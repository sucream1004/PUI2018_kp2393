import os
import json
import sys
import pandas as pd

import urllib.request as urllib

API_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

if not len(sys.argv) == 3:
    print("Wrong number of arguments: It should be python *.py <API_KEY> <BUS_LINE>")
    sys.exit()

#b0e0a9cc-211b-4b03-885c-a01aeeac3e2b

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}".format(API_KEY,BUS_LINE)
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

lat, lon = [], []

bus = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

for i in range(len(bus)):
    lat.append(bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    lon.append(bus[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])

#print("Bus Line: {}\nNumber of Active Buses: {}\nBus {} is at latitude {} and longitude {}").format()
print("Bus Line : {} \nNumber of Active Buses: {}".format(BUS_LINE,len(bus)))
for i in range(len(bus)):
    print("Bus {} is at latitude {} and longitude {}".format(i+1, lat[i], lon[i]))
