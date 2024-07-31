#!/usr/bin/node

const fs = require ('fs');
const arg = process.argv.slice(2);
const fileName = arg[0];

fs.readFile (fileName, 'utf-8', (err, data) => {
  if (err) throw err;
  else {
    console.log(data);
  }
})
