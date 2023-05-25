from flask import Blueprint, render_template, request
from netmiko import ConnectHandler 


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/interfacechanges")
def interface_changes_form():
    return render_template("interface_changes.html")

@views.route("/interfacechanges", methods=["POST", "GET"])
def interface_changes():

    
    if request.method == 'POST':

        data = request.get_json()

        #For the option that the user selected
        select_option = data['select_option']

        #Trunk VLANs
        trunk_port_input = data['trunkPortInput']

        #Access VLAN
        access_port_input = data['accessPortInput']


        ip = str(request.form["ipaddress"])
        port = str(request.form["port"])
        #vlan_number = str(request.form['vlan'])
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




        

        if select_option == 'Trunk':
            vlans = trunk_port_input
            description = description
            interface = port

            result = net_connect.send_command('conf t', expect_string=r'SW1\(config\)#')

            config = [
            
            'int {port}',
            'switchport turnk encapsulation dot1q'
            'switchport mode trunk',
            'switchport trunk allowed vlan {trunk_port_input}',
            'description {description}',
            'exit',
            'exit'

            ]
        elif select_option == 'Access':
            vlan = access_port_input
            description = description
            interface = port

            result = net_connect.send_command('conf t', expect_string=r'SW1\(config\)#')

            config = [
            
            'int {port}',
            'switchport mode access',
            'switchport access vlan {access_port_input}',
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
    

    else:
         return render_template("interfaces_changes.html")
#End of Interface Changes Blueprint

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
