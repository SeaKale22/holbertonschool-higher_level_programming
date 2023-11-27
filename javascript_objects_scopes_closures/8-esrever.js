#!/usr/bin/node

exports.esrever = function (list) {
  // returns a reversed version of the list
  const newList = [];
  const listLenght = list.length;
  for (let i = listLenght - 1; i >= 0; i--) {
    const currentElement = list[i];
    newList.push(currentElement);
  }
  return newList;
};
