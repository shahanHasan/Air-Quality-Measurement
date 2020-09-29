#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:59:19 2020.

@author: shahan

"""

import math , datetime , time , random
import pyfirmata

class MQUnifiedSensor(object):
    """
    A class used to represent MQ-X sensors

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
    Setters : setR0, setRL, setA, setB, setRegressionMethod, 
              setVoltResolution, setADC, serialDebug
    Getters : getA, getB, getR0, getRL, getVoltResolution,
              getRegressionMethod, getVoltage
    User Functions : calibrate, readSensor, validateEquation
    """
################## Software Related Macros / Private names #################
    __firstFlag = False
    #__VOLT_RESOLUTION  = 5.0 -> Assign your own
    __RL = 1 # Value in KiloOhms , set based on sensor
    #__ADC_Bit_Resolution = 10 -> Assign your own 
    __regressionMethod = 1 # 1 -> Exponential || 2 -> Linear
    
    __adc, __a, __b, __sensor_volt = None , None , None , None
    __R0, __RS_air, __ratio, __PPM, __RS_Calc = None , None , None , None , None
# =============================================================================
#     __Type : str
#     __BOARD : str
# =============================================================================
    
    
    def __init__(self, BOARD, Voltage_Resolution, ADC_Bit_Resolution, pin, Type):
        """
        Initialize / Constructor.

        Parameters
        ----------
        BOARD : TYPE -> str
        Voltage_Resolution : TYPE -> int
        ADC_Bit_Resolution : TYPE -> int
        pin : TYPE -> int
        Type : TYPE -> str

        Returns
        -------
        None.

        """
        self. __BOARD = BOARD # E.G : "Arduino"
        self.__VOLT_RESOLUTION = Voltage_Resolution
        self.__ADC_Bit_Resolution = ADC_Bit_Resolution
        self.__pin = pin # analog pin , 0 ,1 ,2 ,3 ,4 ...
        self.__Type = Type # E.G : "CUSTOM MQ"
        
    def setA(self, A):
        """
        
        Parameters
        ----------
        A : TYPE -> int
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.__a = A
    
    def setB(self, B):
        self.__b = B
        
    def setR0(self, R0 = 10):
        self.__R0 = R0
    
    def setRL(self, RL = 1):
        self.__RL = RL
        
    def setADC(self, value):
        self.__sensor_volt = (value) * self.__VOLT_RESOLUTION / (pow(2,self.__ADC_Bit_Resolution) - 1)
        self.__adc = value


    def setVoltResolution(self, voltage_resolution = 5):
        self.__VOLT_RESOLUTION = voltage_resolution
        
    
    def setRegressionMethod(self, regression_Method):
        self.__regressionMethod = regression_Method

    def getR0(self):
        return self.__R0
    
    def getRL(self):
        return self.__RL
    
    def getVoltResolution(self):
        return self.__VOLT_RESOLUTION
    
    def getRegressionMethod(self):
        return "Exponential" if(self.__regressionMethod == 1) else "Linear"
    
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
    
    def serialDebug(self, onSetup = False):
        
        if(onSetup):
            print()
            print("*******************************************************************")
            print("MQ sensor reading library for arduino \n" + 
            "Note: remember that all the parameters below can be modified during the program execution with the methods : \n" + 
            "setR0, setRL, setA, setB where you will have to send as parameter the new value, example: mySensor.setR0(20); //R0 = 20KΩ \n" +
            "Authors: Shahan Hasan \n" +
            "Contributors: ___________________replace with names______________________ \n" + 
            "Sensor : {} \n".format(self.__Type) +
            "Supply voltage: {} VDC \n".format(self.__VOLT_RESOLUTION) +
            "ADC Resolution:  {} Bits \n".format(self.__ADC_Bit_Resolution) +
            "R0: {} KΩ \n".format(self.__R0) +
            "RL: {} KΩ".format(self.__RL))
            
            if(self.__regressionMethod == 1):
                print("Model : Exponential")
            else:
                print("Model : Linear")
            print("MQ-Type : " + self.__Type + "\n" +
            "Slope of the graph :       __a {} \n".format(self.__a) +
            "Y intercept of the graph : __b {} \n".format(self.__b) +
            "Development board: " + self.__BOARD) 
        
        else:
            if not self.__firstFlag:
                print("| ******************** " + self.__Type + "********************* | \n" +
                "| ADC_In | Equation_V_ADC | Voltage_ADC |        Equation_RS        |  Resistance_RS  |    EQ_Ratio  | Ratio (RS/R0) | Equation_PPM |     PPM    |")
                self.__firstFlag = True
                
            else:
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    















        