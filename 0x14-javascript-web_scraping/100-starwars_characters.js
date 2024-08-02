#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/people';

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const data = JSON.parse(body).results;
  for (const person of data) {
    for (const movies of person.films) {
      if (movies.includes(id)) {
        console.log(person.name);
      }
    }
  }
});
