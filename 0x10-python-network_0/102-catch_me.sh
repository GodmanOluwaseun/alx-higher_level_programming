#!/bin/bash
#Scripts that makes a request and causes server to respond with custom message.
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
