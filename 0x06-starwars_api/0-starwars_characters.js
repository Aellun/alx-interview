#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command-line arguments
const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

/**
 * Recursively sends requests to each character URL and prints their names.
 * @param {string[]} characterList - List of character URLs.
 * @param {number} index - Current index in the character list.
 */
function sendRequest (characterList, index) {
  // Base case: if index is out of bounds, stop recursion
  if (characterList.length === index) {
    return;
  }

  // Send request to the current character URL
  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characterList, index + 1);
    }
  });
}

// Fetch movie details from the API
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
  } else if (response.statusCode === 200) {
    try {
      // Parse the movie details and extract the character list
      const characterList = JSON.parse(body).characters;
      if (Array.isArray(characterList)) {
        // Start processing characters
        sendRequest(characterList, 0);
      } else {
        console.error('Invalid character list format.');
      }
    } catch (e) {
      console.error('Error parsing movie response:', e);
    }
  } else {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
  }
});
