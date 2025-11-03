import os
import logging

logger = logging.getLogger(__name__)

def get_switch_ports_status():
    """
    Returns sample switch port data for demonstration
    """
    try:
        # Sample data to demonstrate the interface
        return [
            {
                'name': 'GigabitEthernet1/0/1',
                'status': 'connected',
                'vlan': '10',
                'speed': '1000Mb/s',
                'duplex': 'full',
                'description': 'Server Room - Main Server'
            },
            {
                'name': 'GigabitEthernet1/0/2',
                'status': 'notconnect',
                'vlan': '20',
                'speed': 'auto',
                'duplex': 'auto',
                'description': 'Conference Room AP'
            },
            {
                'name': 'GigabitEthernet1/0/3',
                'status': 'connected',
                'vlan': '30',
                'speed': '100Mb/s',
                'duplex': 'full',
                'description': 'Printer - HR Department'
            },
            {
                'name': 'GigabitEthernet1/0/4',
                'status': 'disabled',
                'vlan': 'trunk',
                'speed': 'auto',
                'duplex': 'auto',
                'description': 'Unused Port'
            },
            {
                'name': 'GigabitEthernet1/0/5',
                'status': 'connected',
                'vlan': '10',
                'speed': '1000Mb/s',
                'duplex': 'full',
                'description': 'Development Team Switch'
            }
        ]
    except Exception as e:
        logger.error(f"Error generating sample data: {str(e)}")
        raise Exception(f"Error generating sample data: {str(e)}")