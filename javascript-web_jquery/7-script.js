
const characterDiv = $('#character');
const charUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  method: 'GET',
  success: function (data) {
    characterDiv.text(data.name);
  }
});
