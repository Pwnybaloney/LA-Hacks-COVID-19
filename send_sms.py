# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC3ddd25f3b0751e1402277dbea25ab7b9'
auth_token = '219c42812324a9d158f31d733a7621f5'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body="twilio be wurkin",
         messaging_service_sid='MG293888266321446c593037379a6d6a6a',
         to='+15622159912'
     )


