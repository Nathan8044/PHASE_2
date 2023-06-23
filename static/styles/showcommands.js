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
    console.log(config_file)
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

    .then(reponse => Response.text())
    .then(data => {
        console.log(data)
        console.log(typeof data)
        
        obj = JSON.parse(data)
        console.log(obj)

        var result = obj.result;
        console.log(result);

        const words = result.split(' ')
        console.log(words);

    })

}