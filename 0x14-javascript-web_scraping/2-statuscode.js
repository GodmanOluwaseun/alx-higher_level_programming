#!/usr/bin/node

const args = process.argv.slice(2);
const url = args[0];

const request = new Request(url, {
  METHOD: 'GET'
});

  fetch(request)
    .then(response => {
      console.log('code:' response.status);
    })
});
