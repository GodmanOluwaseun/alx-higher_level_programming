#!/usr/bin/node

const { argv } = require('node:process');

function factorial (a) {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

if (argv.length <= 2) {
  console.log('1');
  process.exit();
}

const a = Number(argv[2]);
const fac = factorial(a);
console.log(fac);
