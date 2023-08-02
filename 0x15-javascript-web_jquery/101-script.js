// Function to add a new element to the list
function addItem() {
  const newItem = $('<li>Item</li>'); // Create a new <li> element
  $('ul.my_list').append(newItem); // Append the new <li> element to the list
}

// Function to remove the last element from the list
function removeItem() {
  $('ul.my_list li:last-child').remove(); // Remove the last <li> element from the list
}

// Function to clear all elements from the list
function clearList() {
  $('ul.my_list').empty(); // Remove all child elements from the list
}

// Event listeners to handle user clicks on specific <div> elements
$(document).ready(function() {
  // When the user clicks on DIV#add_item, call the addItem function
  $('#add_item').on('click', function() {
    addItem();
  });

  // When the user clicks on DIV#remove_item, call the removeItem function
  $('#remove_item').on('click', function() {
    removeItem();
  });

  // When the user clicks on DIV#clear_list, call the clearList function
  $('#clear_list').on('click', function() {
    clearList();
  });
});
