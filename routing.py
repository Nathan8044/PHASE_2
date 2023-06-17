from flask import Blueprint, render_template, request, redirect, jsonify, make_response
from flask_wtf import FlaskForm, csrf
from netmiko import ConnectHandler


routing_blueprint = Blueprint(__name__, 'routing')

@routing_blueprint.route("/routing", methods=["POST", "GET"])

def routing():

    return render_template("routing.html")
@routing_blueprint.route("/routing/config", methods=["POST"])
def routing_config(): 
    if request.method == 'POST':
        config_file = request.get_json()
        routing_protocol = config_file['routing_protocol']
        ip = config_file['ipaddress']
        username = config_file['username']
        password = config_file['password']
        enable_password = config_file['secret']


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


        if routing_protocol == 'next_hop':
            destination_network = config_file['destination_network']
            destination_subnet = config_file['destination_subnet']
            next_hop_address = config_file['next_hop_address']

            config = [
                "ip route {destination_network} {destination_subnet} {next_hop_address}"
            ]
            config_commands = '\n'.join(config).format(destination_network=destination_network, destination_subnet=destination_subnet, next_hop=next_hop_address)
        elif routing_protocol == 'exit_interface':
            destination_network = config_file['destination_network']
            destination_subnet = config_file['destination_subnet']
            exit_interface = config_file['exit_interface']

            config =[
                "ip route {destination_network} {destination_subnet} {exit_interface}"

            ]

            config_commands = '\n'.join(config).format(destination_network=destination_network, destination_subnet=destination_subnet, exit_interface=exit_interface)
        elif routing_protocol == 'fully_specified':
            destination_network = config_file['destination_network']
            destination_subnet = config_file['destination_subnet']
            next_hop_address = config_file['next_hop_address']
            exit_interface = config_file['exit_interface']

            config = [
                "ip route {destination_network} {destination_subnet} {exit_interface} {next_hop_address}"
            ]

            config_commands = '\n'.join(config).format(destination_network=destination_network, destination_subnet=destination_subnet, next_hop_address=next_hop_address, exit_interface=exit_interface)

        elif routing_protocol == 'rip':

            destination_network = config_file['destination_network']

            config =[
                "router rip"
                "no auto-summary"
                "version 2"
                "network {destination_network}"
            ]
            config_commands = '\n'.join(config).format(destination_network=destination_network)


            
        output = net_connect.send_config_set(config_commands,read_timeout=10000)
        
        #gets the show run comand
        result = net_connect.send_command('sh ip int brief',read_timeout=120)

        return render_template("routing.html", result=result)
    else:

        return render_template("routing.html")
