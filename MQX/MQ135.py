#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:41:16 2020.

@author: shahan
"""

from MQUnifiedSensor import MQUnifiedSensor
import math 


class MQ4():
    """
    
    A class used to represent MQ-4 sensor.

    Attributes
    ----------
    BOARD : TYPE -> str 
        A formatted string to print out the name of the Board i.e Arduino 
    Voltage_Resolution : TYPE -> int
        The voltage resolution of the sensors
    ADC_Bit_Resolution : TYPE -> int
        Analog to Digital bit resolution
    pin : TYPE -> int
        Analog pin on ADC or Arduino
    Type : TYPE -> str
        A formatted string to print out the type of sensor i.e MQ-4 

    Methods
    -------
    Setters : From MQUnified
    Getters : From MQUnified , PPM
    User Functions : calibrate, Main, PPM
    Exponential regression:
  
    Gas    | a      | b
    LPG    | 3811.9 | -3.113
    CH4    | 1012.7 | -2.786
    CO     | 200000000000000 | -19.05
    Alcohol| 60000000000 | -14.01
    smoke  | 30000000 | -8.308
  
    """
    
    def __init__(self):
        self.MQ4 = MQUnifiedSensor("Arduino", 5, 1, 3, "MQ4")
        self.RatioMQ4CleanAir = 4.4
        self.MQ4.setRegressionMethod(1)
        self.MQ4.setA(1012.7)
        self.MQ4.setB(-2.786)
        
    def calibrate(self):
        """
        Calibrate R0.
        
        Methane PPM.

        Returns
        -------
        None.

        """
        print("Calibrating please wait.")
        calcR0 = 0
        for i in range(0,10):
            self.MQ4.update()
            calcR0 += self.MQ4.calibrate(self.RatioMQ4CleanAir)
        
        self.MQ4.setR0(calcR0/10)
        print("Done!!")
        if(math.isinf(calcR0)):
            print("Warning: Conection issue founded, R0 is infite (Open circuit detected) please check your wiring and supply")
        if(calcR0 == 0):
            print("Warning: Conection issue founded, R0 is zero (Analog pin with short circuit to ground) please check your wiring and supply")
        
        self.MQ4.serialDebug(True)

    def main(self):
        """
        Void Main function.

        Returns
        -------
        None.

        """
        self.calibrate()
        while True: 
            self.MQ4.update()
            #print("analog value : {}".format(Analog_value))
            self.MQ4.readSensor()
            self.MQ4.serialDebug()
            #time.sleep(0.1)
        
    def PPM(self):
        """
        Calculate and return PPM  foro MQ4 Sensor.

        Returns
        -------
        PPM : TYPE -> Double
            DESCRIPTION. -> Gas Concentration.

        """
        self.calibrate()
        self.MQ4.update()
        PPM = self.MQ4.readSensor()
        return PPM
        
        
            
if __name__ == "__main__":
    MQ4S = MQ4()
    #MQ4.calibrate()
    MQ4S.main()