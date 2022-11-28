#! /bin/bash

curl -X POST https://api.twilio.com/2010-04-01/Accounts//Messages.json \
                --data-urlencode "Body=testing" \
                --data-urlencode "From=+12137725021" \
                --data-urlencode "To=+1" \
                -u :aa91f359a3fd7ccbdc6e6388e76828d9