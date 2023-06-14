// all javascript for other elements that are not included in bootstrap 


// start of interface_changes access and trunk port options
var selectBox = document.getElementById('selectBox');
var trunk_port = document.getElementById('trunk_port_div');

//// -- for option 2 trunk port 
selectBox.addEventListener('change', function() {
  var selectedOption = selectBox.value;
    if (selectedOption === 'option2') {
      trunk_port.classList.remove('d-none');
    } else {
      trunk_port.classList.add('d-none');
    }
  });

//// -- for option 1 access port 
var selectBox = document.getElementById('selectBox');
var access_port = document.getElementById('access_port_div');

selectBox.addEventListener('change', function() {
  var selectedOption = selectBox.value;
    if (selectedOption === 'option1') {
    access_port.classList.remove('d-none');
    }  else {
      access_port.classList.add('d-none');
    }
  });
//  end of interface_changes access and trunk port options 


var option1 = document.getElementById('yes_speed_policy');
var option2 = document.getElementById('no_speed_policy');
var content1 = document.getElementById('content1');


option1.addEventListener('click', function() {
  content1.classList.remove('hidden');

});

option2.addEventListener('click', function() {
  content1.classList.add('hidden');

});

var option1 = document.getElementById('yes_ip_add');
var option2 = document.getElementById('no_ip_add');
var contentYesIp = document.getElementById('content_yes_ip');


option1.addEventListener('click', function() {
  contentYesIp.classList.remove('hidden');

});

option2.addEventListener('click', function() {
  contentYesIp.classList.add('hidden');

});

function sendconfig() {
  var csrfToken = document.querySelector('input[name="csrf_token"]').value;
  console.log(csrfToken)

  var ipaddress = document.getElementById('ipaddress');
  var username = document.getElementById('username');
  var password = document.getElementById('password');
  var secret = document.getElementById('secret');
  var port = document.getElementById('port');
  var selectedOption = document.getElementById('selectBox');
  var VLANS = document.getElementById('trunk_port');
  var VLAN = document.getElementById('access_port');
  var description = document.getElementById('description');
  var speedlimit = document.getElementById('speedLimit');
  var ip_add = document.getElementById('add_ip');
  var subnet = document.getElementById('subnet');

  var config_file = {
    ipaddress: ipaddress.value,
    username: username.value,
    password: password.value,
    secret: secret.value,
    port: port.value,
    selectedOption: selectedOption.value,
    VLANS: VLANS.value,
    VLAN: VLAN.value,
    description: description.value,
    speedlimit: speedlimit.value,
    ip_add: ip_add.value,
    subnet: subnet.value


  }

  console.log(config_file);

  fetch(`${window.origin}/interfacechanges/config`,{
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify(config_file),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
      'X-CSRFToken': csrfToken,

    })



  })
}

// all javascript for other elements that are not included in bootstrap 


// start of interface_changes access and trunk port options
var selectBox = document.getElementById('selectBox');
var trunk_port = document.getElementById('trunk_port_div');

//// -- for option 2 trunk port 
selectBox.addEventListener('change', function() {
  var selectedOption = selectBox.value;
    if (selectedOption === 'option2') {
      trunk_port.classList.remove('d-none');
    } else {
      trunk_port.classList.add('d-none');
    }
  });

//// -- for option 1 access port 
var selectBox = document.getElementById('selectBox');
var access_port = document.getElementById('access_port_div');

selectBox.addEventListener('change', function() {
  var selectedOption = selectBox.value;
    if (selectedOption === 'option1') {
    access_port.classList.remove('d-none');
    }  else {
      access_port.classList.add('d-none');
    }
  });
//  end of interface_changes access and trunk port options 


var option1 = document.getElementById('yes_speed_policy');
var option2 = document.getElementById('no_speed_policy');
var content1 = document.getElementById('content1');


option1.addEventListener('click', function() {
  content1.classList.remove('hidden');

});

option2.addEventListener('click', function() {
  content1.classList.add('hidden');

});

var option1 = document.getElementById('yes_ip_add');
var option2 = document.getElementById('no_ip_add');
var contentYesIp = document.getElementById('content_yes_ip');


option1.addEventListener('click', function() {
  contentYesIp.classList.remove('hidden');

});

option2.addEventListener('click', function() {
  contentYesIp.classList.add('hidden');

});

function interface_change_config() {
  var csrfToken = document.querySelector('input[name="csrf_token"]').value;
  console.log(csrfToken)

  var ipaddress = document.getElementById('ipaddress');
  var username = document.getElementById('username');
  var password = document.getElementById('password');
  var secret = document.getElementById('secret');
  var port = document.getElementById('port');
  var selectedOption = document.getElementById('access_or_trunk');
  var VLANS = document.getElementById('trunk_port');
  var VLAN = document.getElementById('access_port');
  var description = document.getElementById('description');
  var speedlimit = document.getElementById('speedLimit');
  var ip_add = document.getElementById('add_ip');
  var subnet = document.getElementById('subnet');

  var config_file = {
    ipaddress: ipaddress.value,
    username: username.value,
    password: password.value,
    secret: secret.value,
    port: port.value,
    selectedOption: selectedOption.value,
    VLANS: VLANS.value,
    VLAN: VLAN.value,
    description: description.value,
    speedlimit: speedlimit.value,
    ip_add: ip_add.value,
    subnet: subnet.value


  }

  console.log(config_file);

  fetch(`${window.origin}/interfacechanges/interfacechanges/entry`,{
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify(config_file),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json",
      'X-CSRFToken': csrfToken,

    })



  })
}













