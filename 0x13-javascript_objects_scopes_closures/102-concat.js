#!/usr/bin/node

const fs = require('fs');
const contentA = fs.readFileSync(process.argv[2], 'utf-8', function (err, result) {
  if (err) { console.log(err); }
});
const contentB = fs.readFileSync(process.argv[3], 'utf-8', function (err, result) {
  if (err) { console.log(err); }
});
const contentC = contentA.concat(contentB);
fs.writeFile(process.argv[4], contentC, 'utf-8', function (err, result) {
  if (err) { console.log(err); }
});
