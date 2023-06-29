#!/bin/bash

# Script that takes in a URL and displays all HTTP methods the server will accept

# Send an OPTIONS request to the URL and extract the Allow header
response=$(curl -sI -X OPTIONS "$1" | grep -i "Allow" | awk '{print $2}')

# Display the list of HTTP methods accepted by the server
echo "$response"
