#!/bin/bash
# Script that takes in a URL, sends a request, and displays the size
# Send a request to the URL and extract the Content-Length header
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
