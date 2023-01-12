# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:27:40 2023

@author: Matt
"""

import serial
ser = serial.Serial('COM3', 9600)

while True:
    data = ser.readline()
    if data:
        print(data)
