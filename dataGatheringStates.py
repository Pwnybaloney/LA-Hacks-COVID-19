import http.client
import mimetypes

import json

phoneNumber = '+15622159912'
areaCode = phoneNumber[2:5]
areaState = 'AB'

stateAbrToStateFull = {
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
######################################
conn = http.client.HTTPSConnection("corona.lmao.ninja")
payload = ''
headers = {}
conn.request("GET", "/states", payload, headers)
res = conn.getresponse()
data = res.read()

parsed_json = (json.loads(data))




##############################################################3
#import data for turning state abbreviations into their full names
################################################################3
with open('codes.json') as json_file:
    stateCodes = json.load(json_file)

#print(json.dumps(stateCodes, indent=4, sort_keys=True))

#######################################
#match area codes to their respective states
#########################################
for item in stateCodes:
    for i,j in item.items():
        if areaCode == i:
            areaState = stateCodes[0][i]
print(areaState)


##############################################
#Turn state abbreviations into full state names
############################################

for i in stateAbrToStateFull:
    if areaState == i:
        areaState = stateAbrToStateFull[i]

########################################
#match the state to the full corona database with the amount of cases
####################################
for item in parsed_json:
    for j in item.items():
        if (j[1] == areaState):
            print(areaState + "currently has " + str(parsed_json[0]['cases']) + " cases.")







#for i in stateCodes[0]:
    #stateCode = stateCodes[0]
        #areaState = stateCodes[0][i]
    #print( == stateCodes[0])


#print(json.dumps(stateCodes, indent=4, sort_keys=True))


#    print(json.dumps(stateNames, indent=4, sort_keys=True))

#print(columns[0])
#print(areaCode)
