#!/usr/bin/node

exports.add = function add (a, b) {
  if (typeof a !== 'number' || typeof b !== 'number') {
    console.log('Arguments must be int');
    return;
  }
  const sum = a + b;
  return sum;
};
