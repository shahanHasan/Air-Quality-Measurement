#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 03:18:48 2020.

@author: shahan
"""
#import sys
#sys.path.append('/PMSensor/')
from PMSensor.pmsensor import PMS
import httplib
import urllib
import time


key = "182ENGDTZ0WMJUPT"  # Put your API Key here

def sendData():
	while True:
		#Calculate CPU temperature of Raspberry Pi in Degrees C
		pms = PMS() # Get Raspberry Pi air quality data
		#pm = pms.sensor_read()
		print("Begin")
		pms.sensor_wake()
		time.sleep(15)
		pm = pms.sensor_read()
		if pm is not None:
			params = urllib.urlencode({'field1': pm[0], 'field2': pm[1], 'key':key })
			#param2 = urllib.urlencode({'field2': pm[1], 'key':key })
			print("parameters taken")
			headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
			conn = httplib.HTTPConnection("api.thingspeak.com:80")
			try:
				
				conn.request("POST", "/update", params, headers)
				response = conn.getresponse()
				print("----try catch 1 ------")				
				print("PM2.5 : " + pm[0])
				print("PM10 : " + pm[1])
				print(response.status, response.reason)
				data = response.read()
				conn.close()
			except:
				print("connction failed") 

			pms.sensor_sleep()
			time.sleep(15)
    
if __name__ == "__main__":
	sendData()
