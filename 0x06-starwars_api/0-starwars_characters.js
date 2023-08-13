#!/usr/bin/node

const request = require('request');

const base_url = 'https://swapi-api.hbtn.io/api';

const fetchCharacters = (actors, index) => {
  if (index === actors.length) return;

  const characterUrl = actors[index];
  request(characterUrl, (err, res, body) => {
    if (err) throw err;

    const characterData = JSON.parse(body);
    console.log(characterData.name);

    fetchCharacters(actors, index + 1);
  });
};

request(`${base_url}/films/${process.argv[2]}`, (err, res, body) => {
  if (err) throw err;

  const actors = JSON.parse(body).characters;
  fetchCharacters(actors, 0);
});