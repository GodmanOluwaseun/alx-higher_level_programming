#!/usr/bin/node

const str = 'C is fun';
const { argv } = require('node:process');

if (argv.length <= 2 || isNaN(Number(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const count = Number(argv[2]);
  if (count < 0) {
    process.exit();
  }
  for (let i = 0; i < count; i++) {
      console.log(str);
  }
}
