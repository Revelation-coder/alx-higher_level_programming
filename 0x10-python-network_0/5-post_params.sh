#!/bin/bash

# Script that takes in a URL, sends a POST request with parameters, and displays the body

# Accept the URL as a command line argument
url=$1

# Set the POST parameters in variables
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with the parameters and store the response body in a variable
response=$(curl -s -X POST -d "email=$email&subject=$subject" "$url")

# Display the body of the response
echo "$response"

