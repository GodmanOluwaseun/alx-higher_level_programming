#!/bin/bash
#Script that sends request & displays only the status code of the response.
curl -s -o dev/null -w "%{http_code}" "$1"
