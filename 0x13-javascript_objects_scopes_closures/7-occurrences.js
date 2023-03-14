#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach((val) => {
    if (searchElement === val) {
      count++;
    }
  });
  return count;
};
