import os
import json
import sys
import pandas as pd

import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Wrong number of arguments: It should be python *.py <API_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

API_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
FILE_NAME = sys.argv[3]

#b0e0a9cc-211b-4b03-885c-a01aeeac3e2b

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(API_KEY,BUS_LINE)
print("BEEP..Beep making csv from {}".format(url))
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

lat, lon, stopName, stopStatus = [], [], [], []

bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

for i in range(len(bus)):
    lat.append(bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    lon.append(bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    stopName.append(bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
    stopStatus.append(bus[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])

#Latitude,Longitude,Stop Name,Stop Status
spam = open(FILE_NAME, "w")
spam.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(len(bus)):
    spam.write("{},{},{},{}\n".format(lat[i],lon[i],stopName[i],stopStatus[i]))
