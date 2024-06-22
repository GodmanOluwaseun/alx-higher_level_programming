#!/usr/bin/node

function arraylength (arr) {
  let count = 0;

  arr.forEach(() => {
    count++;
  });
  return count;
}

const { argv } = require('node:process');

let length = arraylength(argv);

if (length <= 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
