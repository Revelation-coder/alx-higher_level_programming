#!/bin/bash
# Script to send JSON POST request and display response body

url="$1"
filename="$2"

# Check if the file is a valid JSON
if ! jq . "$filename" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request and display the response body
response=$(curl -s -X POST -H "Content-Type: application/json" --data @"$filename" "$url")
echo "$response"
