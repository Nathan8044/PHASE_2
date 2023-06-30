function login_config () {
    var user_name = document.getElementById('user_name').value
    var pass_word = document.getElementById('pass_word').value
    localStorage.setItem('username', user_name)
    localStorage.setItem('password', pass_word)
}
function validateForm() {
    var userNameInput = document.getElementById('user_name');
    var passwordInput = document.getElementById('pass_word');
    
    if (userNameInput.value === '' || passwordInput.value === '') {
        alert('Please enter both username and password.');
    } else {
        login_config();
        window.location.href = "/home"; // Redirect to the desired page
    }
}