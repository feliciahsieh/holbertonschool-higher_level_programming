#!/bin/bash
# Send a GET request to URL and display body of the response
curl -sw "%{http_code}" $1

#!/bin/bash
# Send a request to a URL and display size fo the response body
curl -Gs $1
if [ curl -sw "%{http_code}" -o /dev/null 0.0.0.0:5000 -eq 200 ]
then
    curl -sG 0.0.0.0:5000
fi
