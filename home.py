from flask import Blueprint, request, render_template
from netmiko import ConnectHandler 


def ssh_connection():
    pass

@home_blueprint.route("/")
def home_form():
    return render_template("index.html")

@home.route("/", methods=["POST"])
def home():

 #we currently don't want to do anything in home. It should not return anything 

 pass


#interface changes function
@interface_changes_blueprint.route("/")
def interface_changes_form():
    return render_template("interfaces_changes.html")

@interface_changes.route("/", methods=["POST"])
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

    


    return render_template("index.html", result=result)
   
    
#vlan changes function
'''
#this is an example of how to write a function for a new page with new changes and connections to the other .html pages

@vlan_changes_blueprint.route("/")
def vlan_changes_form():
    return render_template("vlan_changes.html")
'''

