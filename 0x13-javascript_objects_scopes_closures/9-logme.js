#!/usr/bin/node

let index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`);
  index += 1;
};
