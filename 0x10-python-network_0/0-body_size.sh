#!/bin/bash
# Send a request to a URL and display size fo the response body
curl -sw "%{size_download}" $1 -o /dev/null | grep -oE '[0-9]+$' | tail -1
