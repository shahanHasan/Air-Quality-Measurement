#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sun Sep 20 03:18:48 2020."""

import time , os , sys
from PMSensor.pmsensor import PMS
from BMP280.BMPTest import BMS
from MQX.MQ7 import MQ7 # CO
from MQX.MQ4 import MQ4 # CH4
from MQX.MQ131 import MQ131 # O3
from MQX.MQ135 import MQ135 # NH4 and CO2
import CSVTest
import ThinkSpeakTest

class DataTransmission():
    """Send data to Think speak and save to CSV file actual."""
    
    def sendData():
        """
        Send data to Think Speak and save to CSV.
    
        Returns
        -------
        None.
    
        """
        #PM sensor object.
        pms = PMS()
        #BME sensor object.
        bms = BMS()
        #MQX sensor object.
        MQ4S = MQ4("CH4")
        MQ7S = MQ7("CO")
        MQ131S = MQ131("O3")
        MQ135NH4 = MQ135("NH4")
        MQ135CO2 = MQ135("CO2")
        #print CSV Head.
        CSVTest.CSVHead()

        while True:
            #BMP sensor read value.
            temp , pres , hum = bms.readFunc()
            
            #PM sensor read value.
            pm = pms.reading()
            
            #MQ sensor read value.
            CH4 = MQ4S.PPM()
            CO = MQ7S.CorrectedPPM()
            O3 = MQ131S.CorrectedPPM()
            NH4 = MQ135NH4.CorrectedPPM()
            CO2 = MQ135CO2.CorrectedPPM()
            # Send and save data.
            CSVTest.saveToCsv(pm[0],pm[1],temp,pres,hum,O3,NH4,CO,CH4,CO2)
            ThinkSpeakTest.thingspeakconn(pm[0],pm[1],temp , pres , O3, NH4, CO, CH4)
            
            print("pm2.5 : {}, Pm10 : {}, temp : {}, pres : {}, hum : {},".format(pm[0],pm[1],temp , pres , hum)
                 +" O3 : {}, NH4 : {}, CO : {} , CH4 : {}, CO2 : {}".format(O3, NH4, CO, CH4, CO2))
            time.sleep(2)
    
if (__name__ == "__main__"):
    
    try:
        data = DataTransmission()
        data.sendData()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
