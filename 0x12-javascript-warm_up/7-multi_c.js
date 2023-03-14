#!/usr/bin/node

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  let i;
  for (i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
