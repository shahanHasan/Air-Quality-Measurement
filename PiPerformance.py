#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sat Oct  3 16:57:24 2020."""

import CSVTest
import ThinkSpeakTest
import time , sys , os
from PMSensor.pmsensor import PMS
from BMP280.BMPTest import BMS
from MQX.MQ7 import MQ7 # CO
from MQX.MQ4 import MQ4 # CH4
from MQX.MQ131 import MQ131 # O3
from MQX.MQ135 import MQ135 # NH4 and CO2

class performance():
    """Testing pi Performance"""
    def __init__(self):
        #Sensor init.
        self.pms = PMS()#DHT
        self.bms = BMS()#BMP
        #MQX
        self.MQ4S = MQ4("CH4")
        self.MQ7S = MQ7("CO")
        self.MQ131S = MQ131("O3")
        self.MQ135NH4 = MQ135("NH4")
        self.MQ135CO2 = MQ135("CO2")
        self.__numberofsamples = 20
        
    def data(self):
        #BMP sensor
        temp , pres , hum = self.bms.readFunc()
        
        #PM sensor
        pm = self.pms.reading()
        
        #MQ sensor
        CH4 = self.MQ4S.PPM()
        CO = self.MQ7S.CorrectedPPM()
        O3 = self.MQ131S.CorrectedPPM()
        NH4 = self.MQ135NH4.CorrectedPPM()
        CO2 = self.MQ135CO2.CorrectedPPM()
        return temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 
    
    def performanceCSV(self):
    #Sensor init 
        
        startcsv = time.time()
        for _ in range(self.__numberofsamples):
            temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 = self.data()
            CSVTest.CSVHead()
            CSVTest.saveToCsv(self.pm[0],self.pm[1],self.temp, self.pres, self.hum, 
                              self.O3, self.NH4, self.CO, self.CH4, self.CO2)
        endcsv = time.time()
        return startcsv, endcsv
    
    def performanceTS(self):
        startTs = time.time()
        for _ in range(self.__numberofsamples):
            temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 = self.data()
            ThinkSpeakTest.thingspeakconn(pm[0],pm[1],temp , pres , O3, NH4, CO, CH4)
            endTs = time.time()
        return startTs, endTs
    
    
    def performanceWhole(self):
        
        startWp = time.time()
        for _ in range(self.__numberofsamples):
            temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 = self.data()
            CSVTest.CSVHead()
            CSVTest.saveToCsv(self.pm[0],self.pm[1],self.temp, self.pres, self.hum, 
                          self.O3, self.NH4, self.CO, self.CH4, self.CO2)
            ThinkSpeakTest.thingspeakconn(pm[0],pm[1],temp , pres , O3, NH4, CO, CH4)
        endWp = time.time()
        return startWp, endWp
        
    
    def main(self, timeInSec):
        
        startcsv, endcsv = self.performanceCSV()
        timecsv = endcsv - startcsv + timeInSec
        startTs, endTs = self.performanceTS()
        timeTs = endTs - startTs + timeInSec
        startWp, endWp = self.performanceWhole()
        timeWp = endWp - startWp + timeInSec
        
        print("Execution time for CSV : {} , Execution time for Think Speak : {} , Execution time for Pi(Both CSV and Think Speak)  : {}".format(timecsv,timeTs,timeWp))
            
        
        
if __name__ == "__main__":
    
    try:
        start = time.time()
        perf = performance()
        end = time.time()
        time = end - start
        perf.main(time)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)   

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        