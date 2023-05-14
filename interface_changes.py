from flask import Blueprint, request, render_template
from netmiko import ConnectHandler 


interface_changes_blueprint = Blueprint(__name__, "interface_changes")

#Start of Interface Changes Blueprint
@interface_changes.route("/")
def interface_changes_form():
    return render_template("interfaces_changes.html")

@interface_changes_blueprint.route("/", mnethods=["POST"])
def interface_changes():
    ip = str(request.form["ipaddress"])
    port = str(request.form["port"])
    vlan_number = str(request.form['vlan'])
    description = str(request.form["description"])
    username = str(request.form["username"])
    password = str(request.form["password"])
    enable_password = str(request.form["secret"])
    device = {
    	'device_type': 'cisco_ios',
    	'ip': ip,
    	'username': username,
    	'password': password,
    	'secret': enable_password,
    	'verbose': True,
    	'global_delay_factor': 2
    }

    net_connect = ConnectHandler(**device)

    net_connect.enable()

    output = net_connect.send_command('show run',expect_string=r'SW1#')




    interface = port
    vlan = vlan_number
    description = description

    result = net_connect.send_command('conf t', expect_string=r'SW1\(config\)#')

    config = [
    
        'int {port}',
    'switchport mode access',
    'switchport access vlan {vlan_number}',
    'description {description}',
    'exit',
    'exit'

    ]
    
    config_commands = '\n'.join(config).format(port=interface, vlan_number=vlan, description=description)

    output = net_connect.send_config_set(
        config_commands,
    read_timeout=10000
    )


    
    result = net_connect.send_command(

        'sh ip int brief',
    read_timeout=120
    )

    


    return render_template("interfaces_changes.html", result=result)
#End of Interface Changes Blueprint
    


