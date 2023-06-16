from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler


interfacechanges_blueprint= Blueprint(__name__, "interfacechanges")




@interfacechanges_blueprint.route("/interfacechanges", methods=['POST', 'GET'])
def interfacechanges():
    print("test from /interfacechanges")
    
    return render_template("interface_changes.html")


@interfacechanges_blueprint.route("/interfacechanges/config", methods=['POST'])

def create_entry():

    if request.method == 'POST':
        #Get data from Fetch api
        config_dict = request.get_json()
        print(config_dict)
        #All data will be coming from the fetch api post request

        ip = config_dict['ipaddress']
        port = config_dict['port']
        username = config_dict['username']
        password = config_dict['password']
        enable_password = config_dict['secret']
        ip_add = config_dict['ip_add']
        subnetMask = config_dict['subnet']
        speedLimit = config_dict['speedlimit']
        VLAN = config_dict['VLAN']
        VLANS = config_dict['VLANS']
        description = config_dict['description']
        port_type = config_dict['selectedOption']


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
        #Enters a show run command 

        
        #takes the fetch port_type data and puts it into a variable
        trunk_config = 'option2'
        access_config = 'option1'

        #the if and else statement used for which vlan input to use One VLAN or many 
 
        if port_type == access_config:
            config = [

                "int {port}",
                "switchport mode {port_type}",
                "switchport {port_type} vlan {vlan}",
                "ip add {ipAddress} {subnetMask}",
                "description {description}",
                "no shut",
                "exit",
                "exit"

            ]
            config_commands = '\n'.join(config).format(port=port, port_type=port_type, vlan=VLAN, ipAddress=ip_add, subnetMask=subnetMask, description=description)
        elif port_type == trunk_config:
            config = [

                "int {port}",
                "switchport trunk encapsulation dot1q",
                "switchport mode {port_type}",
                "switchport {port_type} allowed vlan {vlans}",
                "ip add {ipAddress} {subnetMask}",
                "description {description}",
                "no shut",
                "exit",
                "exit"
            ]
            config_commands = '\n'.join(config).format(port=port, port_type=port_type, vlans=VLANS, ipAddress=ip_add, subnetMask=subnetMask, description=description)
            

        
        #formats and send the commands to the device
        

            


        output = net_connect.send_config_set(config_commands,read_timeout=10000)


        #gets the show run comand
        result = net_connect.send_command('sh ip int brief',read_timeout=120)

        


        return render_template("interfaces_changes.html", result=result)
    

    else:
         return render_template("interfaces_changes.html")
