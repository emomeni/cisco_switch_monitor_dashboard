# Network Monitoring Dashboard

A Flask-based web application for monitoring Cisco switch ports status with real-time updates and basic authentication.

## Features

- Real-time monitoring of switch port status
- Basic authentication system with login/logout
- Auto-refresh functionality (60-second intervals)
- Responsive design using Bootstrap
- Color-coded status indicators
- Port details including VLAN, speed, and duplex settings

## Project Structure

```
├── app.py                 # Main Flask application
├── main.py                # Entry point
├── models.py              # Database models
├── forms.py               # Form definitions
├── switch_manager.py      # Switch port status management
├── pyproject.toml         # Python project’s metadata and dependencies in a standardised way
├── static/
│   ├── css/
│   │   └── custom.css     # Custom styles
│   └── js/
│       └── dashboard.js   # Dashboard functionality
└── templates/
    ├── base.html          # Base template
    ├── login.html         # Login page
    └── dashboard.html     # Main dashboard
```

## Requirements

- Python 3.11+
- Flask and extensions:
  - flask-login
  - flask-sqlalchemy
  - flask-wtf
- PostgreSQL (or SQLite for development)
- Additional packages listed in requirements.txt

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cisco_switch_monitor_dashboard.git
cd cisco_switch_monitor_dashboard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables:
```bash
export SESSION_SECRET="your-secret-key"
export DATABASE_URL="postgresql://user:password@localhost/dbname"  # Optional, defaults to SQLite
```

4. Run the application:
```bash
python main.py
```

The application will be available at `http://localhost:5000`

## Default Login

- Username: admin
- Password: admin

## Features

### Authentication
- Secure login system with password hashing
- Session management
- Protected routes

### Dashboard
- Real-time port status display
- VLAN assignments
- Port speed and duplex settings
- Port descriptions
- Auto-refresh functionality

### Responsive Design
- Bootstrap-based layout
- Mobile-friendly interface
- Clean and modern UI

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Example Dashboard

Here is an example of the dashboard showing interface status:

![Dashboard screenshot](images/dashboard.png)

and this is the Login Page:

![Port detail screenshot](images/login-page.png)
