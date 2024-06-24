#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 2 || isNaN(Number(argv[2]))) {
  console.log('Missing size');
}

const size = (Number(argv[2]));

if (size < 0) {
  process.exit();
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
