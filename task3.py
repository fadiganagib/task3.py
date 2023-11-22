from netmiko import ConnectHandler
import pexpect

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.101',
    'username': 'prne',
    'password': 'cisco123!',
    'secret': 'class123!',

}

# Create SSH session
session = pexpect.spawn('ssh ' + 'username' + '@' + 'ip', encoding='utf-8', timeout=20)
result = session.expect(['password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exits then display error and exit
if result != 0:
    print('---- failure! creating session for: ', 'ip')
    exit()

# Connect to the device
R1 = device
device = ConnectHandler
device.enable()
session.sendline('enable')
result = session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

# Check for error, if exits then display error and exit
if result != 0:
    print('---- Failure! entering enable mode')
    exit()
with ConnectHandler(**R1) as net_connect:

    # Enter enable mode
    net_connect.enable()

    # Configure OSPF
    ospf_config = [
        'router ospf 1',
        'network 192.168.56.101 0.0.0.255 area 0',
        'network 192.168.57.101 0.0.0.255 area 0',
        'network 192.168.58.101 0.0.0.255 area 0',
        'exit',

    ]

    # Send OSPF configuration commands

    output = net_connect.send_config_set(ospf_config)
    print('output')

    # save the configuration
    net_connect.save_config()








    
    
    
