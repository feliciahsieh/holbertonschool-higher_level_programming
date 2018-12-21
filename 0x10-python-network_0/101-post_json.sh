#!/bin/bash
# send POST request to URL with data in file and show body of the response
curl -sH "Content-Type: application/json" --request POST --data @$2 "$1"
