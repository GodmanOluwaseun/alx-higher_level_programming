#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length <= 2) {
  console.log('Not a number');
} else if (!isNaN(Number(argv[2]))) {
  console.log('My number:' argv[2]);
} else {
  console.log('Not a number');
}
