// Function to fetch and display the translation of "hello" in French
function fetchHelloTranslation() {
  // URL to fetch the translation
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

  // Fetch data from the URL
  $.get(url, function(data) {
    const translation = data.hello; // Extract the "hello" translation from the fetched data
    const $helloDiv = $('#hello'); // Select the DIV element to display the translation

    // Set the content of the DIV element to the fetched translation
    $helloDiv.text(translation);
  });
}

// Call the function to fetch and display the translation
fetchHelloTranslation();
