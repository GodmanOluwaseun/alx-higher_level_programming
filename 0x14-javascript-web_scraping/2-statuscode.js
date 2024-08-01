#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);
const url = args[0];

request(url, {method: 'GET'}, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    process.exit(1);
  } else {
    console.log('code:', response.statusCode);
  }
});
