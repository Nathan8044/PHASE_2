from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler
from flask import jsonify 
from werkzeug.utils import secure_filename
import os

upload_blueprint = Blueprint(__name__, 'upload')

@upload_blueprint.route("/upload", methods=['POST', 'GET'])

def upload ():
    return render_template("upload.html")

@upload_blueprint.route("/upload/config", methods=['POST'])
def upload_config(): 

    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')
        enable_password = request.form.get('secret')
        selectedOption = request.form.get('selectedOption')

        #SSH connection to the device using Netmiko and the device dictionary above 

        csv_file = request.files['csvFile']
        filename = secure_filename(csv_file.filename)
        csv_file.save(filename)
        print(csv_file)


        try: 
            file = open(filename, "r")
        except FileNotFoundError: 
            return "The wrong file was submitted or file was not found"
        
        file.readline()


        for line in file:
            config_line = line.strip()
            config_line = line.split(',')


            device = {
                'device_type': 'cisco_ios',
                'ip': config_line[0],
                'username': username,
                'password': password,
                'secret': enable_password,
                'verbose': True,
                'global_delay_factor': 2
            }
            net_connect = ConnectHandler(**device)

            net_connect.enable()
            if selectedOption == 'add':

                config = [
                    'int {port}',
                    'switchport mode access',
                    'switchport access vlan {vlan}',
                    'service-policy input POLICE-{speed_policy}M-IN',
                    'service-policy output POLICE-{speed_policy}M-OUT',
                    'description {description}',
                    'exit',
                    'exit',
                ]
            elif selectedOption == 'remove': 

                config = [
                    'int {port}',
                    'no switchport mode access',
                    'no switchport access vlan {vlan}',
                    'no service-policy input POLICE-{speed_policy}M-IN',
                    'no service-policy output POLICE-{speed_policy}M-OUT',
                    'no description {description}',
                    'exit',
                    'exit',
                ]

            config_commands = '\n'.join(config).format(port=config_line[1], vlan=config_line[3], speed_policy=config_line[2], description=config_line[4]) 


            output = net_connect.send_config_set(
                config_commands,
                cmd_verify=False,  # Disable command verification
                read_timeout=10000,
                delay_factor=2
                )            


        


        return jsonify(result = 'Change Successful')
    

    else:
         return render_template("interfaces_changes.html")