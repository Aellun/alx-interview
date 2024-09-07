#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

// Check if a Movie ID is provided
if (process.argv.length > 2) {
  // Fetch movie details
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.error('Error fetching movie details:', err);
      return;
    }

    // Parse the response body to get the list of character URLs
    const charactersURL = JSON.parse(body).characters;

    // Create an array of Promises for fetching each character's details
    const charactersName = charactersURL.map(url => new Promise((resolve, reject) => {
      request(url, (promiseErr, __, charactersReqBody) => {
        if (promiseErr) {
          reject(new Error('Error fetching character: ' + promiseErr.message));
        } else {
          try {
            // Parse character details and resolve with the name
            resolve(JSON.parse(charactersReqBody).name);
          } catch (parseErr) {
            reject(new Error('Error parsing character response: ' + parseErr.message));
          }
        }
      });
    }));

    // Wait for all character details to be fetched and print names
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error('Error fetching some character details:', allErr));
  });
} else {
  console.error('Please provide a Movie ID.');
}
