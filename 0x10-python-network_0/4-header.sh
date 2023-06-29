#!/bin/bash

# Script that takes in a URL, sends a GET request with a custom header, and displays the body

# Accept the URL as a command line argument
url=$1

# Send a GET request to the URL with the custom header and store the response body in a variable
response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response"
