import os
import logging
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///network.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Import models and initialize db
from models import db, User
db.init_app(app)

# Import other dependencies
from forms import LoginForm
from switch_manager import get_switch_ports_status

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except Exception as e:
        logger.error(f"Error loading user: {e}")
        return None

# Create default admin user if not exists
def create_default_user():
    try:
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            user = User(
                username='admin',
                email='admin@example.com',
                password_hash=generate_password_hash('admin')
            )
            db.session.add(user)
            db.session.commit()
            logger.info("Created default admin user")
    except Exception as e:
        logger.error(f"Error creating default user: {e}")
        db.session.rollback()

# Routes
@app.route('/')
@login_required
def dashboard():
    try:
        ports = get_switch_ports_status()
        logger.debug(f"Retrieved {len(ports)} ports")
        return render_template('dashboard.html', ports=ports)
    except Exception as e:
        logger.error(f"Error fetching switch ports: {str(e)}")
        flash(f"Error fetching switch data: {str(e)}", 'danger')
        return render_template('dashboard.html', ports=[])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                logger.info(f"User {user.username} logged in successfully")
                next_page = request.args.get('next')
                return redirect(next_page or url_for('dashboard'))
            flash('Invalid username or password', 'danger')
        except Exception as e:
            logger.error(f"Login error: {e}")
            flash('An error occurred during login', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/api/ports')
@login_required
def get_ports():
    try:
        ports = get_switch_ports_status()
        return {'success': True, 'data': ports}
    except Exception as e:
        logger.error(f"Error fetching switch ports: {str(e)}")
        return {'success': False, 'error': str(e)}

# Initialize the application
with app.app_context():
    try:
        logger.info("Initializing application...")
        create_default_user()
        logger.info("Application initialization complete")
    except Exception as e:
        logger.error(f"Error during application initialization: {e}")