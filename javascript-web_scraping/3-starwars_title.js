#!/usr/bin/node

const request = require('request');

const episodeId = process.argv[2];

const requestUrl = 'https://swapi-api.hbtn.io/api/films/' + episodeId;

function printEpTitle (err, response, body) {
  if (err) {
    // do nothing
  }
  const epData = JSON.parse(body);
  console.log(epData.title);
}

request(requestUrl, printEpTitle);
