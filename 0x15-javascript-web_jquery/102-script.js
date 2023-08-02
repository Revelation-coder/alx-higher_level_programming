// Function to fetch and print the translation of "Hello"
function fetchHelloTranslation() {
  const languageCode = $('#language_code').val(); // Get the language code from the input field
  const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`; // URL with the language code

  // Fetch data from the URL
  $.get(url, function(data) {
    const translation = data.hello; // Extract the "hello" translation from the fetched data
    const $helloDiv = $('#hello'); // Select the DIV element to display the translation

    // Set the content of the DIV element to the fetched translation
    $helloDiv.text(translation);
  });
}

// Event listener to handle user click on the "Translate" button
$(document).ready(function() {
  $('#btn_translate').on('click', function() {
    fetchHelloTranslation();
  });
});
