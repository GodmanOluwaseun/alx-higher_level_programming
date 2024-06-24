#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log('NaN');
}

function add(a, b) {
  a = Number(argv[2]);
  b = Number(argv[3]);
  let sum = a + b;
  console.log(sum);
}

add(argv[2], argv[3]);
