#!/usr/bin/node

const { argv } = require('node:process');

if (argv[2] <= 2 || isNaN(Number(argv[2]))) {
  console.log('Missing size');
}

const size = argv[2];

if (size < 0) {
  process.exit();
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      console.log('X');
    }
    console.log('');
  }
}
