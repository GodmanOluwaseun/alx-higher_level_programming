#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  if (argv.length <= 3) {
    console.log(NaN);
    process.exit();
  } else {
      a = Number(argv[2]);
      b = Number(argv[3]);
      const sum = a + b;
      console.log(sum);
  }
}

add(argv[2], argv[3]);
