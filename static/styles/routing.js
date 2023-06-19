//start of option selector 
var selectBox = document.getElementById('selectBox');
var next_hop = document.getElementById('next_hop_input');


selectBox.addEventListener('change', function() {
    var selectedOption = selectBox.value
    if (selectedOption == 'next_hop') {
        next_hop.classList.remove('d-none')
    } else {
        next_hop.classList.add('d-none')
    }
})

var exit_interface = document.getElementById('exit_interface_input');

selectBox.addEventListener('change', function() {
    var selectedOption = selectBox.value
    if (selectedOption == 'exit_interface') {
        exit_interface.classList.remove('d-none');
    } else {
        exit_interface.classList.add('d-none');
    }
})

var fully_specified = document.getElementById('fully_specified_input');

selectBox.addEventListener('change', function() {
    var selectedOption = selectBox.value;
    if (selectedOption == 'fully_specified') {
        fully_specified.classList.remove('d-none');
    } else {

        fully_specified.classList.add('d-none');
    }
})

var rip = document.getElementById('rip_input');

selectBox.addEventListener('change', function() {
    var selectedOption = selectBox.value;
    if (selectedOption == 'rip') {
        rip.classList.remove('d-none');
    } else {
        rip.classList.add('d-none')
    }
})
// end of option selector



// start of routing config fucntion for submit button
function routing_config() {
    var csrfToken = document.querySelector('input[name="csrf_token"]').value;
    var ipaddress = document.getElementById('ipaddress');
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var secret = document.getElementById('secret');
    var selectedOption = document.getElementById('selectBox').value

    // conditional statements to decided which route to choose 
    if (selectedOption == 'next_hop') {
        var destination_network = document.getElementById('destination_network1');
        var destination_subnet = document.getElementById('destination_subnet1');
        var next_hop_address = document.getElementById('next_hop_value1');
        config_file = {
            ipaddress: ipaddress.value,
            username: username.value,
            password: password.value, 
            secret: secret.value,
            routing_protocol: selectedOption,
            destination_network: destination_network.value,
            destination_subnet: destination_subnet.value,
            next_hop_address: next_hop_address.value
        } 
    } else if (selectedOption == 'exit_interface') {
        var destination_network = document.getElementById('destination_network2');
        var destination_subnet = document.getElementById('destination_subnet2');
        var exit_interface = document.getElementById('exit_interface_value2');
            config_file = {
                ipaddress: ipaddress.value,
                username: username.value,
                password: password.value, 
                secret: secret.value,
                routing_protocol: selectedOption,
                destination_network: destination_network.value, 
                destination_subnet: destination_subnet.value, 
                exit_interface: exit_interface.value
                }
    } else if (selectedOption == 'fully_specified') {
        var destination_network = document.getElementById('destination_network3');
        var destination_subnet = document.getElementById('destination_subnet3');
        var exit_interface = document.getElementById('exit_interface_value3');
        var next_hop_address = document.getElementById('next_hop_value3');
        config_file = {
            ipaddress: ipaddress.value,
            username: username.value,
            password: password.value, 
            secret: secret.value,
            routing_protocol: selectedOption,
            destination_network: destination_network.value,
            destination_subnet: destination_subnet.value,
            next_hop_address: next_hop_address.value,
            exit_interface: exit_interface.value
        }
    } else if (selectedOption == 'rip') {
        var destination_network = document.getElementById('destination_network4');
        config_file = {
            ipaddress: ipaddress.value,
            username: username.value,
            password: password.value, 
            secret: secret.value,
            routing_protocol: selectedOption,
            destination_network: destination_network.value
        }
    }
    console.log(config_file)
    fetch(`${window.origin}/routing/routing/config`, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(config_file),
        cache: 'no-cache',
        headers: new Headers ({
            "content-type": "application/json",
            'X-CSRFToken': csrfToken
        })



    })

    
}
// end of routing config function
