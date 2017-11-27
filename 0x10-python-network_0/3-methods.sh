#!/bin/bash
# Display all HTTP methods server will accept for user's URL
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'
