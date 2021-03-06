#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sun Sep 20 03:18:48 2020."""
#import sys
#sys.path.append('/PMSensor/')
import httplib
import urllib
import time, sys ,os
from PMSensor.pmsensor import PMS
from BMP280.BMPTest import BMS
from MQX.MQ7 import MQ7 # CO
from MQX.MQ4 import MQ4 # CH4
from MQX.MQ131 import MQ131 # O3
from MQX.MQ135 import MQ135 # NH4 and CO2

key = "182ENGDTZ0WMJUPT"  # Put your API Key here
Number_of_samples = 20

def thingspeakconn(sense1,sense2,sense3,sense4,sense5,sense6,sense7,sense8):
    """
    Think Speak set up.
    
    Parameters
    ----------
    sense1 : TYPE -> double
        DESCRIPTION. -> Sensor data
    sense2 : TYPE
        DESCRIPTION.
    sense3 : TYPE
        DESCRIPTION.
    sense4 : TYPE
        DESCRIPTION.
    sense5 : TYPE
        DESCRIPTION.
    sense6 : TYPE
        DESCRIPTION.
    sense7 : TYPE
        DESCRIPTION.
    sense8 : TYPE
        DESCRIPTION.
    sense9 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    params = urllib.urlencode(
         {'field1': sense1, 
          'field2': sense2,
          'field3': sense3, 
          'field4': sense4, 
          'field5': sense5,
          'field6': sense6,
          'field7': sense7, 
          'field8': sense8, 
          'key':key })
    #param2 = urllib.urlencode({'field2': pm[1], 'key':key })
    #print("parameters taken")
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    try:
        #print("----try catch 1 ------")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        #print("PM2.5 : " + pm[0])
        #print("PM10 : " + pm[1])
        #print(response.status, response.reason)
        data = response.read()
        conn.close()
    except:
        print("connction failed")
        #print("why???")
        
        
        
        
def sendData():
    """
    Send data to Think Speak.

    Returns
    -------
    None.

    """
    pms = PMS()
    
    bms = BMS()
    
    MQ4S = MQ4("CH4")
    MQ7S = MQ7("CO")
    MQ131S = MQ131("O3")
    MQ135NH4 = MQ135("NH4")
    MQ135CO2 = MQ135("CO2")
    

    for _ in range(Number_of_samples):
        #print("Begin")
        #BMP sensor
        temp , pres , hum = bms.readFunc()
        
        #PM sensor
        pm = pms.reading()
    
        #MQ sensor
        CH4 = MQ4S.PPM()
        CO = MQ7S.CorrectedPPM()
        O3 = MQ131S.CorrectedPPM()
        NH4 = MQ135NH4.CorrectedPPM()
        CO2 = MQ135CO2.CorrectedPPM()
        
        thingspeakconn(pm[0],pm[1],temp , pres , O3, NH4, CO, CH4)
        print("pm2.5 : {}, Pm10 : {}, temp : {}, pres : {}, hum : {},".format(pm[0],pm[1],temp , pres , hum)
             +" O3 : {}, NH4 : {}, CO : {} , CH4 : {}, CO2 : {}".format(O3, NH4, CO, CH4, CO2))
        time.sleep(0.2)
        
        
        

if (__name__ == "__main__"):
    
    try:
        #start = time.time()
        sendData()
        #end = time.time()
        
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



















        
        
        
        
        
        
        
