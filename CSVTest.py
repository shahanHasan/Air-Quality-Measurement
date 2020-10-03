#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sat Oct  3 14:37:05 2020."""

import time, datetime , csv , os , sys
from PMSensor.pmsensor import PMS
from BMP280.BMPTest import BMS
from MQX.MQ7 import MQ7 # CO
from MQX.MQ4 import MQ4 # CH4
from MQX.MQ131 import MQ131 # O3
from MQX.MQ135 import MQ135 # NH4 and CO2

Number_of_samples = 20

def CSVHead():
    """
    Add csv head row.

    Returns
    -------
    None.

    """
    with open("/home/pi/Desktop/Airquality measureAdjusted/CSV/data.csv", 'ab') as csvfile:
        file = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #if(!headerAdded):
        file.writerow(['date and Time','pm2.5','pm10','temperature' , 'pressure' , 'humidity', 'O3', 'NH4', 'CO', 'CH4', 'CO2'])
        csvfile.close()
            

def saveToCsv(sense1,sense2,sense3,sense4,sense5,sense6,sense7,sense8,sense9,sense10):
    """
    Save data to CSV, CSV set up.

    Parameters
    ----------
    sense1 : TYPE -> Float
        DESCRIPTION. -> Sensor Data
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
    with open("/home/pi/Desktop/Airquality measureAdjusted/CSV/data.csv", 'ab') as csvfile:
        file = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([datetime.datetime.now().replace(microsecond=0).isoformat().replace('T', ' '), 
        sense1, sense2, sense3, sense4, sense5,
        sense6,sense7,sense8,sense9,sense10])
        csvfile.close()
        

def saveData():
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
    
    CSVHead()
    for _ in range(Number_of_samples):
        #print("Begin")
        #BMP sensor
        temp , pres , hum = bms.readFunc()
        
        #PM sensor
        pms.sensor_wake()
        time.sleep(5)
        pm = pms.sensor_read()
        
        #MQ sensor
        CH4 = MQ4S.PPM()
        CO = MQ7S.CorrectedPPM()
        O3 = MQ131S.CorrectedPPM()
        NH4 = MQ135NH4.CorrectedPPM()
        CO2 = MQ135CO2.CorrectedPPM()


        saveToCsv(pm[0],pm[1],temp , pres , hum, O3, NH4, CO, CH4, CO2)
        time.sleep(2)
        print("pm2.5 : {}, Pm10 : {}, temp : {}, pres : {}, hum : {},".format(pm[0],pm[1],temp , pres , hum)
             +" O3 : {}, NH4 : {}, CO : {} , CH4 : {}, CO2 : {}".format(O3, NH4, CO, CH4, CO2))


        
if __name__ == "__main__":
    
    try:
        start = time.time()
        saveData()
        end = time.time()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    