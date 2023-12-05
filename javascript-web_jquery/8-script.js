
const movieList = $('#list_movies');

$.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      for (let i = 0; i < data.results.length; i++) {
        let title = '<li>' + data.results[i].title + '</li>';
        movieList.append(title);
      }
    },
    error: function (error) {
        console.log(error);
    }
  });
