#!/usr/bin/node

const value = parseInt(process.argv[2]);
let string = '';

if (isNaN(value)) {
  console.log('Missing size');
} else {
  let i, j;
  for (i = 0; i < value; i++) {
    for (j = 0; j < value; j++) {
      if (j === value - 1 && i === j) {
        string += 'X';
      } else if (j === value - 1 && i !== j) {
        string += 'X\n';
      } else {
        string += 'X ';
      }
    }
  }
  console.log(string);
}
