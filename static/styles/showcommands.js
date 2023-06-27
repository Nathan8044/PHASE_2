function showcommands_config () {
    var csrfToken = document.querySelector('input[name="csrf_token"]').value;


    var selectedOption = document.getElementById('selectBox');
    var ipaddress = document.getElementById('ipaddress');
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var secret = document.getElementById('secret');

    config_file = {
        ipaddress: ipaddress.value,
        username: username.value,
        password: password.value, 
        secret: secret.value,
        selectedOption: selectedOption.value
    }

    fetch(`${window.origin}/showcommands/showcommands_config`, {
        method: 'POST',
        credentials: 'include',
        body: JSON.stringify(config_file),
        cache: 'no-cache',
        headers: new Headers ({
            "content-type": "application/json",
            'X-CSRFToken': csrfToken
        })
        


    })

    .then(response => response.text())
    .then(data => {

        obj = JSON.parse(data)
        var result = obj.result;
        const words = result.split(' ')

        let formattedResult = ''; // Empty variable 
        for (let count = 0; count < words.length; count++ ) {
          formattedResult += words[count] + ' ';


          if ((count + 1) % 6 === 0) {
            formattedResult += '<br>';
          }

        }

        document.getElementById('result').innerHTML = formattedResult; 

    })

}