#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2]; // Get the movie ID from the command-line argument

const base_url = 'https://swapi.dev/api';
const film_endpoint = `films/${movieId}/`;

// Make a request to get information about the selected movie
request(`${base_url}/${film_endpoint}`, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch character names using the character URLs
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.log(`Failed to fetch character data: ${charError}`);
        }
      });
    });
  } else {
    console.log(`Failed to fetch movie data: ${error}`);
  }
});