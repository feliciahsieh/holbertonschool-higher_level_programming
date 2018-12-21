#!/bin/bash
# Send request & receive "You got me!" in body response. Follow redirect with new GET
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
