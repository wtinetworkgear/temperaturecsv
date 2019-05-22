#!/usr/bin/env python3

# This program will read a WTI OOB or PDU device for the temperature every
# minute and format the data as Comma-separated values

import json
import time
import requests
import urllib3

# supress Unverified HTTPS request, only do this is a verified environment
urllib3.disable_warnings()

# Address of the WTI device
URI = "https://"
SITE_NAME = "rest.wti.com"
BASE_PATH = "/api/v2/status/temperature"

# put in the username and password to yuor WTI device here
USERNAME = "rest"
PASSWORD = "restfulpassword"

failcount  = 0
while True:
    try:
        r = requests.get(URI+SITE_NAME+BASE_PATH, auth=(USERNAME, PASSWORD), verify=False)
        if (r.status_code == 200):
            parsed_json = r.json()

#			Uncomment to see the JSON return by the unit
#            print (parsed_json)

            statuscode = parsed_json["status"]["code"]

            if (int(statuscode) == 0):
                temperature = parsed_json['temperature']
                temperatureformat = parsed_json['format']
                timestamp = parsed_json['timestamp']

                print("{0}, {1}, {2}, {3}".format(SITE_NAME, timestamp, temperature, temperatureformat))
                failcount  = 0
            else:
                failcount+=1

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        time.sleep(60)
        failcount+=1

    if (failcount > 10):
        exit(1);
    time.sleep(60)
