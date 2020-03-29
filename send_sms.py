# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

import os
#Set SID and auth tokens
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

#sent the message
message = client.messages \
    .create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         messaging_service_sid='MG293888266321446c593037379a6d6a6a',
         to='+15622159912'
     )

print(message.sid)
