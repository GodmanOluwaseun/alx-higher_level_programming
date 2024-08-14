const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.getJSON(url, function(data) {
  const name = data.name;
  $('#character').text(name);
}).fail(function() {
  console.error('Error');
});
