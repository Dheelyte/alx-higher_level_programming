#!/usr/bin/node

const vals = process.argv;
if (vals.length === 2 || vals.length === 3) {
  console.log(0);
} else {
  vals.forEach((val) => {
    parseInt(val);
  });
  console.log(vals.sort(function (a, b) { return a - b; })[vals.length - 2]);
}
