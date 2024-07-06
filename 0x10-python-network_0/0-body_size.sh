#!/bin/bash
#Takes a URL, sends a request, and displays the size of the body of the response in bytes

if [ '$#' -ne 1]; then
    echo "Usage: $0 url"
fi

content_length=$(curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}' | tr -d '\r')

echo "$content_length"
