const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.getJSON(url, function(data) {
  const movies = data.results;
  for (const movie of movies) {
    $('#list_movies').append(`<li>${movie.title}</li>`);
  }
}).fail(function() {
  console.error('Error');
});
