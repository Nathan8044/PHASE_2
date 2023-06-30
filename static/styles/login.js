function login_config () {
    var user_name = document.getElementById('user_name').value
    var pass_word = document.getElementById('pass_word').value
    localStorage.setItem('username', user_name)
    localStorage.setItem('password', pass_word)
}