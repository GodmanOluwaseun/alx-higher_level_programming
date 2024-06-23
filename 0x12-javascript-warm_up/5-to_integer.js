#!/usr/bin/node

const { argv } = require('node:process');

if (typeof argv[2] === 'number') {
  console.log(argv[2]);
} else if (typeof argv[2] === 'string' && !isNaN(Number(argv[2]))) {
  console.log(Number(argv[2]));
} else if (typeof argv[2] === 'Bigint') {
  console.log(Number(argv[2]);
} else {
  console.log('Not a number');
}
