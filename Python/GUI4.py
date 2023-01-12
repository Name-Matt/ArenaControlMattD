# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:09:33 2023

@author: Matt
"""

import tkinter as tk
from tkinter import ttk
import serial

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600)

# Create main window
window = tk.Tk()
window.title("Arduino Control")

# Create styles used for objects
RedEmergStyle = ttk.Style()
RedEmergStyle.theme_use('classic')
RedEmergStyle.configure('RedEmerg.TButton', background = 'red', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
RedEmergStyle.map('RedEmerg.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', 'red')])
GreenResStyle = ttk.Style()
GreenResStyle.theme_use('classic')
GreenResStyle.configure('GreenRes.TButton', background = 'green', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
GreenResStyle.map('GreenRes.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', 'green')])

# Create emergency stop button
def emergency_stop():
    ser.write(b'E')
    print('Sent emergency stop command')
    stop_button.state(["disabled"])
    resume_button.state(["!disabled"])
    pin4_button.config(state='disabled')
    pin5_button.config(state='disabled')
    pin6_button.config(state='disabled')
    pin7_button.config(state='disabled')
    pin8_button.config(state='disabled')
    pin12_button.config(state='disabled')

stop_button = ttk.Button(window, text="Emergency Stop", command=emergency_stop, style ="RedEmerg.TButton")
stop_button.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Create resume button
def resume():
    ser.write(b'R')
    print('Sent resume command')
    stop_button.state(["!disabled"])
    resume_button.state(["disabled"])
    pin4_button.config(state='normal')
    pin5_button.config(state='normal')
    pin6_button.config(state='normal')
    pin7_button.config(state='normal')
    pin8_button.config(state='normal')
    pin12_button.config(state='normal')

resume_button = ttk.Button(window, text="Resume", command=resume, style ="GreenRes.TButton", state = "disabled")
resume_button.grid(row=1, column=1, padx=10, pady=10, sticky="w")

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

pin4_button = tk.Radiobutton(text="0%", variable=pin_var, value=4)

pin5_button = tk.Radiobutton(text="20%", variable=pin_var, value=5)

pin6_button = tk.Radiobutton(text="40%", variable=pin_var, value=6)

pin7_button = tk.Radiobutton(text="60%", variable=pin_var, value=7)

pin8_button = tk.Radiobutton(text="80%", variable=pin_var, value=8)

pin12_button = tk.Radiobutton(text="100%", variable=pin_var, value=12)

# Line up the buttons in the first column, with one button per row
pin4_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
pin5_button.grid(row=1, column=0, padx=5, pady=5, sticky="w")
pin6_button.grid(row=2, column=0, padx=5, pady=5, sticky="w")
pin7_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")
pin8_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")
pin12_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")


# Close serial port when window is closed
def on_closing():
    ser.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()