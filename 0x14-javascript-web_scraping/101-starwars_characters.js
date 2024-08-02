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
  printOrderly(data, 0);
});

function printOrderly (characters, index) {
  request(characters[index], (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }

    const character = JSON.parse(body).name;
    console.log(character);
    if (index + 1 < characters.length) {
      printOrderly(characters, index + 1);
    }
  });
}
