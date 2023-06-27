function upload_config() {
  var csrfToken = document.querySelector('input[name="csrf_token"]').value;

  var username = document.getElementById('username');
  var password = document.getElementById('password');
  var secret = document.getElementById('secret');
  var selectedOption = document.getElementById('selectBox');

  var fileInput = document.getElementById('formFile');
  var file = fileInput.files[0];

  var formData = new FormData();
  formData.append('username', username.value);
  formData.append('password', password.value);
  formData.append('secret', secret.value);
  formData.append('csvFile', file);
  formData.append('selectedOption', selectedOption.value);

  fetch(`${window.origin}/upload/upload/config`, {
    method: 'POST',
    credentials: 'include',
    body: formData,
    cache: 'no-cache',
    headers: {
      'X-CSRFToken': csrfToken,
    },
  })
    .then((response) => response.text()) // Parse the response as text
    .then((data) => {
      obj = JSON.parse(data);

      document.getElementById('result').innerHTML = obj['result'];
    });
}
