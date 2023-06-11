from flask import Blueprint, render_template, request, redirect, jsonify, make_response
views = Blueprint("views", __name__)
from flask_wtf import FlaskForm, csrf

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/interfacechanges", methods=['POST', 'GET'])
def interfacechanges():
    print("test from /interfacechanges")
    
    return render_template("interface_changes.html")


@views.route("/interfacechanges/entry", methods=['POST'])

def create_entry():
    req = request.get_json()
    print(req)


    # return "thanks"
    # if request.method == 'POST':
    #     #Get data from ajax request
    #     data = request.get_json()
    #     #index data from the ajax request 
    #     select_option = data['select_option']
    #     trunk_port_input = data['trunk_port']
    #     access_port_input = data['access_port']
    #     speed_limit_input = data['speed_limit']
    #     ip_address_input = data['ip_address']
    #     subnet_mask_input = data['subnet_mask']

    #     #get the data below from the HTTP post request in the form. This is not from the ajax request
    #     #converts the normal form data in a a dictionary for SSH connection
    #     ip = str(request.form["ipaddress"])
    #     port = str(request.form["port"])
    #     description = str(request.form["description"])
    #     username = str(request.form["username"])
    #     password = str(request.form["password"])
    #     enable_password = str(request.form["secret"])
    #     device = {
    #         'device_type': 'cisco_ios',
    #         'ip': ip,
    #         'username': username,
    #         'password': password,
    #         'secret': enable_password,
    #         'verbose': True,
    #         'global_delay_factor': 2
    #     }

    #     #SSH connection to the device using Netmiko and the dictionary above 
    #     net_connect = ConnectHandler(**device)

    #     net_connect.enable()
    #     #Enters a show run command 
    #     output = net_connect.send_command('show run',expect_string=r'SW1#')
    #     #takes the ajax data and puts it into a variable
    #     interface = port
    #     port_type = select_option
    #     #the if and else statement used for which vlan input to use One VLAN or many 
    #     if port_type == "Access":
    #         vlan = access_port_input

    #     else: 
    #         vlan = trunk_port_input

    #     #the rest of the variables are converted using variables from the ajax request
    #     speedlimit = speed_limit_input
    #     ipAddress = ip_address_input
    #     subnetMask = subnet_mask_input
    #     description = description
    #     #the nested if and else statements used to differentiate between access and trunk ports
    #     #This is because the commands are different 
    #     if port_type == 'Access':

    #         config = {

    #             "int {port}",
    #             "switchport mode {port_type}",
    #             "switchport {port_type} vlan {vlan}",
    #             "ip add {ipAddress} {subnetMask}",
    #             "description {description}",
    #             "exit",
    #             "exit"

    #         }
    #     else: 

    #         config = {

    #             "int {port}",
    #             "switchport trunk encapsulation dot1q",
    #             "switchport mode {port_type}",
    #             "switchport {port_type} allowed vlan {vlan}",
    #             "ip add {ipAddress} {subnetMask}",
    #             "description {description}",
    #             "exit",
    #             "exit"
    #         }
    #     #formats and send the commands to the device
    #     config_commands = '\n'.join(config).format(port=interface, port_type=port_type, vlan=vlan, ipAddress=ipAddress, subnetMask=subnetMask description=description)

            


    #     output = net_connect.send_config_set(config_commands,read_timeout=10000)


    #     #gets the show run comand
    #     result = net_connect.send_command('sh ip int brief',read_timeout=120)

        


    #     return render_template("interfaces_changes.html", result=result)
    

    # else:
    #      return render_template("interfaces_changes.html")

    
       

@views.route("/interfacesecurity")
def interface_security():
    return render_template("interface_security.html")

@views.route("/routing")
def routing():
    return render_template("routing.html")

@views.route("/globalcommands")
def global_commands():
    return render_template("global_commands.html")

@views.route("/showcommands")
def show_commands():
    return render_template("show_commands.html")

@views.route("/privcommands")
def priv_commands():
    return render_template("priv_commands.html")

@views.route("/upload")
def upload():
    return render_template("upload.html")

@views.route("/loginpage")
def login():
    return render_template("login.html")


