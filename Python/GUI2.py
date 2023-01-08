# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:09:33 2023

@author: Matt
"""

import tkinter as tk
import serial

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600)

# Create main window
window = tk.Tk()
window.title("Arduino Control")

# Create emergency stop button
def emergency_stop():
    ser.write(b'E')
    print('Sent emergency stop command')
    stop_button.config(foreground='white', background='grey', state='disabled')
    resume_button.config(foreground='white', background='green', state='normal')

stop_button = tk.Button(text="Emergency Stop", command=emergency_stop)
stop_button.pack(side='top')
stop_button.config(foreground='white', background='red')

# Create resume button
def resume():
    ser.write(b'R')
    print('Sent resume command')
    stop_button.config(foreground='white', background='red', state='normal')
    resume_button.config(foreground='black', background='grey', state='disabled')

resume_button = tk.Button(text="Resume", command=resume)
resume_button.pack(side='top')
resume_button.config(foreground='black', background='grey', state='disabled')

# Create radio buttons to control Arduino pins
pin_var = tk.IntVar()

def update_pin(name, index, mode):
    pin = pin_var.get()
    if pin == 4:
        ser.write(b'4')
    elif pin == 5:
        ser.write(b'5')
    elif pin == 6:
        ser.write(b'6')
    elif pin == 7:
        ser.write(b'7')
    elif pin == 8:
        ser.write(b'8')
    elif pin == 12:
        ser.write(b'12')

pin_var.trace('w', update_pin)

pin4_button = tk.Radiobutton(text="Pin 4", variable=pin_var, value=4)
pin4_button.pack()

pin5_button = tk.Radiobutton(text="Pin 5", variable=pin_var, value=5)
pin5_button.pack()

pin6_button = tk.Radiobutton(text="Pin 6", variable=pin_var, value=6)
pin6_button.pack()

pin7_button = tk.Radiobutton(text="Pin 7", variable=pin_var, value=7)
pin7_button.pack()

pin8_button = tk.Radiobutton(text="Pin 8", variable=pin_var, value=8)
pin8_button.pack()

pin12_button = tk.Radiobutton(text="Pin 12", variable=pin_var, value=12)
pin12_button.pack()



# Close serial port when window is closed
def on_closing():
    ser.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()