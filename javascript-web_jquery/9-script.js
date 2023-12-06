
$(document).ready(function () {
  const helloDiv = $('#hello');

  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function (data) {
      helloDiv.text(data.hello);
    }
  });
});
