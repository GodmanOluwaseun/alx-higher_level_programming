#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length === 4) {
  console.log(`${argv[3]} is ${argv[4]}`);
} else if (argv.length === 3) {
  console.log(`${argv[3]} is undefined`);
} else if (argv.length <= 2) {
  console.log(`undefined is undefined`);
}
