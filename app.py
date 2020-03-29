from flask import Flask, render_template, request
from twilio.rest import Client

import os

import http.client
import mimetypes

import json

app = Flask(__name__)

string returnString = ""
@app.route('/', methods=['GET'])
def home():
    return render_template('landing.html') ##render the html page

@app.route("/textSend", methods=['GET'])
def sendText():


    toPhoneNumber = request.args.get("phoneNumber") #get the phone number obtained from front end

    account_sid = os.environ['TWILIO_ACCOUNT_SID'] #get account_sid for twilio
    auth_token = os.environ['TWILIO_AUTH_TOKEN'] #get auth token for twilio
    client = Client(account_sid, auth_token)

    #sent the message
    message = client.messages \ #send message through twilio
        .create(
             body="the britsh are coming!",
             messaging_service_sid='MG293888266321446c593037379a6d6a6a',
             to= toPhoneNumber
         )
    ##############################################################

    areaCode = toPhoneNumber[2:5] #parses the area code of the phone number
    areaState = 'AB' #set an initial state

    stateAbrToStateFull = { ##for abbreviations to full name conversions
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }

    #######################################
    #import data for amount of cases by state

    conn = http.client.HTTPSConnection("corona.lmao.ninja")
    payload = ''
    headers = {}
    conn.request("GET", "/states", payload, headers)
    res = conn.getresponse()
    data = res.read()

    parsed_json = (json.loads(data))




    ##############################################################
    #import data for turning state abbreviations into their full names

    with open('codes.json') as json_file:
        stateCodes = json.load(json_file)

    #print(json.dumps(stateCodes, indent=4, sort_keys=True))

    ###########################################################################
    #match area codes to their respective states

    for item in stateCodes:
        for i,j in item.items():
            if areaCode == i:
                areaState = stateCodes[0][i]
    print(areaState)


    ##############################################
    #Turn state abbreviations into full state names using the data


    for i in stateAbrToStateFull:
        if areaState == i:
            areaState = stateAbrToStateFull[i]

    #################################################################
    #match the state to the full corona database with the amount of cases

    for item in parsed_json:
        for j in item.items():
            if (j[1] == areaState):
                returnString = areaState + "currently has " + str(parsed_json[0]['cases']) + " cases."
    return returnString


if __name__ == '__main__':
    app.run(debug=True)
