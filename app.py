from flask import Flask, render_template, request
from twilio.rest import Client

import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('landing.html')

@app.route("/textSend", methods=['GET'])
def sendText():
    toPhoneNumber = request.args.get("phoneNumber")

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    #sent the message
    message = client.messages \
        .create(
             body="the britsh are coming!",
             messaging_service_sid='MG293888266321446c593037379a6d6a6a',
             to= toPhoneNumber
         )

    return message.sid

if __name__ == '__main__':
    app.run(debug=True)
