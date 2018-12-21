#!/bin/bash
# send POST request to URL with data in file and show body of the response
curl -H "Content-Type: application/json" --request POST --data-binary @"$2" "$1"
