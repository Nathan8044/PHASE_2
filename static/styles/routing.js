
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