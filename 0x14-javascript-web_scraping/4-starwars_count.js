#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const film of data) {
      for (const character of film.characters) {
        if (character === id) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
