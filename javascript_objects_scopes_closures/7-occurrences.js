#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // returns number of occurences of searchElement in list
  let elementOccurences = 0;
  const listLength = list.length;
  for (let i = 0; i < listLength; i++) {
    if (list[i] === searchElement) {
      elementOccurences += 1;
    }
  }
  return elementOccurences;
};
