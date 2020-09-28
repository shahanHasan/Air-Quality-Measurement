#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 03:18:48 2020.

@author: shahan
"""

import httplib
import urllib
import time, datetime , csv
from PMSensor.pmsensor import PMS
from BMP280.BMPTest import BMS

key = "182ENGDTZ0WMJUPT"  # Put your API Key here

def saveToCsv(sense1,sense2,sense3,sense4,sense5):
    
    with open('/home/pi/data.csv', 'ab') as csvfile:
        file = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([datetime.datetime.now().replace(microsecond=0).isoformat().replace('T', ' '), sense1, sense2, sense3, sense4, sense5])
        csvfile.close()

def thingspeakconn(sense1,sense2,sense3,sense4,sense5):  
    params = urllib.urlencode(
         {'field1': sense1, 
          'field2': sense2,
          'field3': sense3, 
          'field4': sense4, 
          'field5': sense5,  
          'key':key })
    #param2 = urllib.urlencode({'field2': pm[1], 'key':key })
    print("parameters taken")
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        print("----try catch 1 ------")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print("PM2.5 : " + pm[0])
        #print("PM10 : " + pm[1])
        print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connction failed")
        #print("why???")

#def sensorINIT():
     #Calculate CPU particle , temperature, pressure with Raspberry Pi 
#    pms = PMS() # Get Raspberry Pi air quality data
#    bms = BMS()
    
def sendData():
    pms = PMS()
    bms = BMS()
    
    while True:
        print("Begin")
        
        temp , pres , hum = bms.readFunc()
        pms.sensor_wake()
        time.sleep(10)
        pm = pms.sensor_read()
        if pm is not None:
            saveToCsv(pm[0],pm[1],temp , pres , hum) 
            thingspeakconn(pm[0],pm[1],temp , pres , hum)
            pms.sensor_sleep()
            time.sleep(20)
    
if __name__ == "__main__":
    sendData()
