from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler


global_commands_blueprint = Blueprint(__name__, 'globalcommands')

@global_commands_blueprint.route('/globalcommands', methods=['POST', 'GET'])
def global_commands():

    return render_template('global_commands.html')

@global_commands_blueprint.route('/globalcommands/config', methods=['POST'])
def global_commands_config(): 
    if request.method == 'POST':
        config_file = request.get_json()
        ip = config_file['ipaddress']
        username = config_file['username']
        password = config_file['password']
        enable_password = config_file['secret']
        selectedOption = config_file['selectedOption']

        device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password,
            'secret': enable_password,
            'verbose': True,
            'global_delay_factor': 2
        }

        #SSH connection to the device using Netmiko and the device dictionary above 
        net_connect = ConnectHandler(**device)

        net_connect.enable()
        # option to choose which option will be configured. 
        if selectedOption == 'vlan_name':

            vlan_name = config_file['vlan_name']
            vlan_id = config_file['vlan_id']
	   
            config = [
		"vlan {vlan_id}",
                "name {vlan_name}"
            ]

            config_commands = '\n'.join(config).format(vlan_id=vlan_id, vlan_name=vlan_name)
        elif selectedOption == 'ip_default_gateway':

            ip_default_gateway = config_file['ip_default_gateway']

            config = [

                "ip default-gateway {ip_default_gateway}"
            ]

            config_commands = '\n'.join(config).format(ip_default_gateway=ip_default_gateway)


        output = net_connect.send_config_set(
            config_commands,
            cmd_verify=False,  # Disable command verification
            read_timeout=10000,
            delay_factor=2
            )


        
        #gets the show run comand
        result = net_connect.send_command('sh ip int brief',read_timeout=120)

        return render_template("global_commands.html", result=result)
    else: 
        return render_template("global_commands")
