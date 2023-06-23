from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler
from flask import jsonify 

showcommands_blueprint = Blueprint(__name__, 'showcommands')

@showcommands_blueprint.route('/showcommands', methods=['POST', 'GET'])
def showcommands():

    return render_template('show_commands.html')

@showcommands_blueprint.route('/showcommands_config', methods=['POST'])
def showcommands_config(): 

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

        if selectedOption == 'showrun':
            result = net_connect.send_command('show run',read_timeout=120)

        elif selectedOption == 'showipintbrief':
            result = net_connect.send_command('show ip int brief',read_timeout=120)

        elif selectedOption == 'showmacadd':
            result = net_connect.send_command('show mac address-table',read_timeout=120)

        elif selectedOption == 'shiproute':
            result = net_connect.send_command('show ip route',read_timeout=120)

        elif selectedOption == 'showvlanbrief':
            result = net_connect.send_command('show vlan brief',read_timeout=120)

        elif selectedOption == 'showinttrunk':
            result = net_connect.send_command('show int trunk',read_timeout=120)
        
        print(result)
        return jsonify(result=result)       
    else: 
        return render_template('show_coammands.html')