from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler
from flask import jsonify 



interfacesecurity_blueprint = Blueprint(__name__, "interfacesecurity")

@interfacesecurity_blueprint.route("/interfacesecurity", methods=['POST', 'GET'])
def interfacesecurity():
    return render_template("interface_security.html")


@interfacesecurity_blueprint.route("/interfacesecurity/config", methods=['POST', 'GET'])
def config_entry():
    if request.method == 'POST':
        #Get data from Fetch api
        config_dict = request.get_json()



        ip = config_dict['ipaddress']
        port = config_dict['port']
        username = config_dict['username']
        password = config_dict['password']
        enable_password = config_dict['secret']
        max_devices = config_dict['max_devices']
        violation = config_dict['violation']




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


        config = [

                "int {port}",
                "switchport mode access",
                "switchport port-security maximum {max_devices}",
                "switchport port-security violation {violation}",
                "no shut",
                "exit",
                "exit"

            ]

        config_commands = '\n'.join(config).format(port=port, max_devices=max_devices, violation=violation) 


        output = net_connect.send_config_set(
            config_commands,
            cmd_verify=False,  # Disable command verification
            read_timeout=10000,
            delay_factor=2
            )

        final_command = 'show port-security int ' + port
        #gets the show run comand
        result = net_connect.send_command(final_command, read_timeout=120)

        return jsonify(result = result)
    else: 

        return render_template("interface_security.html")