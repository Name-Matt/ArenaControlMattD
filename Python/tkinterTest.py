# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 17:38:23 2023

@author: Matt
"""

import serial
import tkinter as tk

class ArduinoGUI:
    def __init__(self, master):
        self.arduino = serial.Serial('COM3', 9600)

        self.emergency_stop_button = tk.Button(master, text="Emergency Stop", command=self.emergency_stop)
        self.emergency_stop_button.pack()

        self.pin_var = tk.IntVar()  # initialize pin_var
        self.pin_var.set(0)  # initialize to 0

        self.pin_4_button = tk.Radiobutton(master, text="Pin 4", variable=self.pin_var, value=4, command=self.set_pin)
        self.pin_4_button.pack()
        self.pin_5_button = tk.Radiobutton(master, text="Pin 5", variable=self.pin_var, value=5, command=self.set_pin)
        self.pin_5_button.pack()
        self.pin_6_button = tk.Radiobutton(master, text="Pin 6", variable=self.pin_var, value=6, command=self.set_pin)
        self.pin_6_button.pack()
        self.pin_7_button = tk.Radiobutton(master, text="Pin 7", variable=self.pin_var, value=7, command=self.set_pin)
        self.pin_7_button.pack()
        self.pin_8_button = tk.Radiobutton(master, text="Pin 8", variable=self.pin_var, value=8, command=self.set_pin)
        self.pin_8_button.pack()
        self.pin_12_button = tk.Radiobutton(master, text="Pin 12", variable=self.pin_var, value=12, command=self.set_pin)
        self.pin_12_button.pack()

        self.update_pins()  # update the radio buttons with the current state of the pins

    def emergency_stop(self):
        self.arduino.write(b'E')  # send emergency stop signal to Arduino

    def set_pin(self):
        pin = self.pin_var.get()
        if pin != 0:
            self.arduino.write(bytes([pin]))  # send pin number to Arduino

    def update_pins(self):
        self.arduino.write(b'R')  # request the state of the pins from the Arduino
        state = self.arduino.read()  # read the state of the pins from the Arduino
        self.pin_var.set(state)  # update the radio buttons with the current state of the pins
        self.after(1000, self.update_pins)  # update the radio buttons every 1000 milliseconds (1 second)

root = tk.Tk()
app = ArduinoGUI(root)
root.mainloop()



