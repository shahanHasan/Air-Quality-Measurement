#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sun Oct  4 05:08:15 2020"""

import threading
import time , os , sys
from PMSensor.pmsensor import PMS
from BMP280.BMPTest import BMS
from MQX.MQ7 import MQ7 # CO
from MQX.MQ4 import MQ4 # CH4
from MQX.MQ131 import MQ131 # O3
from MQX.MQ135 import MQ135 # NH4 and CO2
import CSVTest
import ThinkSpeakTest
from PiPerformance import performance


perf = performance()
# temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 = perf.data()
# csvlist = []
# thinkspeaklist = []
# csvlist.extend([pm[0],pm[1],temp,pres,hum,O3,NH4,CO,CH4,CO2])
# thinkspeaklist.extend(pm[0],pm[1],temp , pres , O3, NH4, CO, CH4)

class ThreadCSV (threading.Thread, ):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

      
   def run(self):
      print("Starting " + self.name)
      while True:
          CSV_write()
      #print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)
      


class ThreadTS (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

      
   def run(self):
      print("Starting " + self.name)
      while True:
          TS_send()
      #print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)


def CSV_write():
    while True:
        temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 = perf.data()
        CSVTest.saveToCsv(pm[0],pm[1],temp,pres,hum,O3,NH4,CO,CH4,CO2)

def TS_send():
    while True:
        temp , pres , hum , pm , CH4 , CO , O3 , NH4 , CO2 = perf.data()
        ThinkSpeakTest.thingspeakconn(pm[0],pm[1],temp , pres , O3, NH4, CO, CH4)
        
def main():
    # Create new threads
    thread1 = ThreadCSV(1, "Thread-CSV")
    thread2 = ThreadTS(2, "Thread-Think Speak")

    # Start new Threads
    thread1.start()
    thread2.start()


if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print('Finished')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)  




































