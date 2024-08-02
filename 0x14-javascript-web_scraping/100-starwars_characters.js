#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + id, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }

  const data = JSON.parse(body).characters;
  for (const person of data) {
    request(person, (err, response, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      const data2 = JSON.parse(body);
      console.log(data2.name);
    });
  }
});
