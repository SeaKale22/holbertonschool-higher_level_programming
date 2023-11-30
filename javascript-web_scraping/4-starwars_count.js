#!/usr/bin/node

const request = require('request');
const requestUrl = process.argv[2];

function countWedgeMovies (err, response, body) {
  if (err) {
    // do nothing
  }
  const data = JSON.parse(body);
  const moviesList = data.results;
  let count = 0;
  for (let i = 0; i < 7; i++) {
    const currentMovie = moviesList[i];
    const movieChars = currentMovie.characters;
    if (movieChars.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
}

request(requestUrl, countWedgeMovies);
