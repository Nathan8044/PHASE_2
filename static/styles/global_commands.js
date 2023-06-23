var selectBox = document.getElementById('selectBox');
var selectedOption = selectBox.value;


// checks for which option is clicked 
var vlan_name_form = document.getElementById('vlan_name_form');
selectBox.addEventListener('change', function () {
    var selectedOption = selectBox.value;

    if (selectedOption == 'vlan_name') {
        vlan_name_form.classList.remove('d-none');
    } else {
        vlan_name_form.classList.add('d-none');
    }
})
var ip_default_gateway_form = document.getElementById('ip_default_gateway_form');
selectBox.addEventListener('change', function () {
    var selectedOption = selectBox.value;

    if (selectedOption == 'ip_default_gateway') {
        ip_default_gateway_form.classList.remove('d-none');
    } else {
        ip_default_gateway_form.classList.add('d-none')
    }
})


// start of function to send config
function global_commands_config() {

    var csrfToken = document.querySelector('input[name="csrf_token"]').value;
    var ipaddress = document.getElementById('ipaddress');
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var secret = document.getElementById('secret');
    var selectedOption = document.getElementById('selectBox').value





    if (selectedOption == 'vlan_name') {
        var vlan_id = document.getElementById('vlan_id');
        var vlan_name = document.getElementById('vlan_name');

        config_file = {
            ipaddress: ipaddress.value,
            username: username.value,
            password: password.value, 
            secret: secret.value,
            selectedOption: selectedOption,
            vlan_id: vlan_id.value,
            vlan_name: vlan_name.value
        }
    } else if (selectedOption == 'ip_default_gateway') {
        var ip_default_gateway = document.getElementById('ip_default_gateway');

        config_file = {
            ipaddress: ipaddress.value,
            username: username.value,
            password: password.value, 
            secret: secret.value,
            selectedOption: selectedOption,
            ip_default_gateway: ip_default_gateway.value
        }

    }
    console.log(config_file)
    fetch(`${window.origin}/globalcommands/globalcommands/config`, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(config_file),
        cache: 'no-cache',
        headers: new Headers ({
            "content-type": "application/json",
            'X-CSRFToken': csrfToken
        })
        


    })

    .then(response => response.text())  // Parse the response as text
    .then(data => {
        // Intitial data is a string
	    obj = JSON.parse(data);
        // Converts string to object since it was already 
        console.log(obj)
        // You can check out the type of the element
        console.log(typeof obj)

        // Index the obj to use it 
        var result = obj.result;
        console.log(result);
        // Split based on spaces and new lines 
        const words = result.split(' ');
        console.log(words);
        // Intialize new variable 
        let formattedResult = ''; // Renamed the variable
        // For loop through the words string to format it to the html 
        for (let count = 0; count < words.length; i++) {
          formattedResult += words[count] + ' ';
          console.log(formattedResult);
          
          if ((i + 1) % 6 === 0) {
            formattedResult += '<br>';
          }
        }
        
        console.log(formattedResult);
        document.getElementById('result').innerHTML = words;
      })
}
// end of function to send config 