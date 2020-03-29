# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC3ddd25f3b0751e1402277dbea25ab7b9'
auth_token = 'c04c20800d88d25f1efc401b3245200b'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="wubbalubbadubdub.",
         messaging_service_sid='MG293888266321446c593037379a6d6a6a',
         to='+15627326959'
     )

print(message.sid)
