function interface_security_config() {
    var csrfToken = document.querySelector('input[name="csrf_token"]').value;
    console.log(csrfToken)
  
    var ipaddress = document.getElementById('ipaddress');
    var username = document.getElementById('username');
    var password = document.getElementById('password');
    var secret = document.getElementById('secret');
    var port = document.getElementById('port');
    var max_devices = document.getElementById('max_devices');
    var violation = document.getElementById('violation');
  
    var config_file = {
      ipaddress: ipaddress.value,
      username: username.value,
      password: password.value,
      secret: secret.value,
      port: port.value,
      max_devices: max_devices.value,
      violation: violation.value,
    }
    console.log(config_file);
    fetch(`${window.origin}/interfacesecurity/interfacesecurity/config`,{
      method: 'POST',
      credentials: 'include',
      body: JSON.stringify(config_file),
      cache: "no-cache",
      headers: new Headers({
        "content-type": "application/json",
        'X-CSRFToken': csrfToken,
  
      })
  
  
  
    })

    // .then(response => response.text())
    // .then(data => {

      
    // })
  
  }