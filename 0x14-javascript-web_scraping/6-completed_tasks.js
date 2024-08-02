#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  const data = JSON.parse(body);

  const completed = {};

  for (const i of data) {
    if (i.completed === true) {
      if (completed[i.userId]) {
        completed[i.userId]++;
      } else {
        completed[i.userId] = 1;
      }
    }
  }
  console.log(completed);
});
