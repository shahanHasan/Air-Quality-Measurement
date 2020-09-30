#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 17:41:16 2020

@author: shahan
"""

from MQUnifiedSensor import MQUnifiedSensor
import math , time
import pyfirmata

board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

pin = 3
analog_input = board.get_pin('a:{}:i'.format(pin))

MQ4 = MQUnifiedSensor("Arduino", 5, 10, 3, "MQ4")
RatioMQ4CleanAir = 4.4
MQ4.setRegressionMethod(1)
MQ4.setA(1012.7)
MQ4.setB(-2.786)

# =============================================================================
#    Exponential regression:
#   Gas    | a      | b
#   LPG    | 3811.9 | -3.113
#   CH4    | 1012.7 | -2.786
#   CO     | 200000000000000 | -19.05
#   Alcohol| 60000000000 | -14.01
#   smoke  | 30000000 | -8.308
# =============================================================================


print("Calibrating please wait.")
calcR0 = 0
for i in range(0,10):
    MQ4.update(analog_input)
    calcR0 += MQ4.calibrate(RatioMQ4CleanAir)

MQ4.setR0(calcR0/10)
print("Done!!")
if(math.isinf(calcR0)):
    print("Warning: Conection issue founded, R0 is infite (Open circuit detected) please check your wiring and supply")
if(calcR0 == 0):
    print("Warning: Conection issue founded, R0 is zero (Analog pin with short circuit to ground) please check your wiring and supply")

MQ4.serialDebug(True)


while True:
    MQ4.update(analog_input)
#    print("analog value : {}".format(Analog_value))
    MQ4.readSensor()
    MQ4.serialDebug()
    time.sleep(0.1)
    