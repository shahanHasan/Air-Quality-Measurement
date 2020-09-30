#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:02:29 2020.

@author: shahan
"""
from MQX.MQ4 import MQ4 # CH4
from MQX.MQ7 import MQ7 # CO
from MQX.MQ131 import MQ131 # O3
from MQX.MQ135 import MQ135 # NH4 and CO2


def main():
    MQ4S = MQ4("CH4")
    MQ7S = MQ7("CO")
    MQ131S = MQ131("O3")
    MQ135NH4 = MQ135("NH4")
    MQ135CO2 = MQ135("CO2")
    
    while True:
        #MQ sensor
        CH4 = MQ4S.PPM()
        CO = MQ7S.PPM()
        O3 = MQ131S.PPM()
        NH4 = MQ135NH4.PPM()
        CO2 = MQ135CO2.PPM()
        print("CH4 : {} CO : {} O3 : {} NH4 : {} CO2 : {}".format(CH4, CO, O3, NH4, CO2))