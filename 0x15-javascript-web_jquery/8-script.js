// Function to fetch and list movie titles
function fetchMovies() {
  // URL to fetch movie data
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Fetch data from the URL
  $.get(url, function(data) {
    const movies = data.results; // Extract the movies array from the fetched data
    const $list = $('#list_movies'); // Select the UL element to append movie titles

    // Loop through the movies array and append each title to the UL element
    movies.forEach(function(movie) {
      const title = movie.title;
      $list.append(`<li>${title}</li>`);
    });
  });
}

// Call the function to fetch and list movie titles
fetchMovies();
