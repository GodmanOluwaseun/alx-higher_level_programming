#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 3) {
  console.log('0');
  process.exit();
}

const intArray = argv.slice(2).map(value => Number(value));
intArray.sort((a, b) => a - b);
console.log(intArray[intArray.length - 2]);
