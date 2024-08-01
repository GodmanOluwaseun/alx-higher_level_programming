#!/usr/bin/node

const fs = require('fs');
const args = process.argv.slice(2);
const filePath = args[0];
let string = args[1];

fs.writeFile(filePath, string, 'utf-8', (err) => {
  if (err) throw err;
  });
