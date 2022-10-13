#! bin/bash/

curl -X POST https://api.twilio.com/2010-04-01/Accounts/ACc694da8ac49970a09c99ff6a81f6b872/Messages.json \
                --data-urlencode "Body=$2" \
                --data-urlencode "From=+12137725021" \
                --data-urlencode "To=+1$1" \
                -u ACc694da8ac49970a09c99ff6a81f6b872:aa91f359a3fd7ccbdc6e6388e76828d9