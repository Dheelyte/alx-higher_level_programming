#!/usr/bin/node

const array = require('./100-data').list;
const mappedArray = array.map(x => x * array.indexOf(x));
console.log(array);
console.log(mappedArray);
