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

# Set up padding and location varaibles
radioButtonsPadX = 10
radioButtonsPadY = 5
buttonPadX = 10
buttonPadY = 1
framePad = 2
radioButtonColumn = 0   #spin button locations
radioButtonRow = 2
CTButtonColumn = 1  #Corner Trap button locations
CTButtonRow = 2
GMButtonColumn = 2  #Game Mode button locations
GMButtonRow = 2

# Create a boarder around the spin speed radio buttons
spin_frame = tk.Frame(window, bg='pink', bd=1, relief='solid')
spin_frame.grid(row=radioButtonRow, column=radioButtonColumn, rowspan=7, padx=framePad, pady=framePad, sticky='nsew')

# Create a boarder around the corner trap buttons
CT_frame = tk.Frame(window, bg='green', bd=1, relief='solid')
CT_frame.grid(row=CTButtonRow, column=CTButtonColumn, rowspan=5, padx=framePad, pady=framePad, sticky='nsew')

# Create a boarder around the game mode buttons
GM_frame = tk.Frame(window, bg='blue', bd=1, relief='solid')
GM_frame.grid(row=GMButtonRow, column=GMButtonColumn, rowspan=7, padx=framePad, pady=framePad, sticky='nsew')

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
stop_button.grid(row=0, column=0, columnspan = 3, padx=buttonPadX, pady=buttonPadY, sticky="nsew")

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
resume_button.grid(row=1, column=0, columnspan = 3, padx=buttonPadX, pady=buttonPadY, sticky="nsew")

# Create corner trap enable button
def CT_enb():
    ser.write(b'C')
    print('Sent enable corner trap command')
    CT_enb_button.state(["disabled"])
    CT_disb_button.state(["!disabled"])


CT_enb_button = ttk.Button(window, text="LOWER", command=CT_enb, style ="RedEmerg.TButton")
CT_enb_button.grid(row=CTButtonRow+1, column=CTButtonColumn, rowspan=2, padx=buttonPadX, pady=buttonPadY, sticky="w")

# Create corner trap disable button
def CT_disb():
    ser.write(b'D')
    print('Sent resume command')
    CT_enb_button.state(["!disabled"])
    CT_disb_button.state(["disabled"])

CT_disb_button = ttk.Button(window, text="RAISE", command=CT_disb, style ="GreenRes.TButton", state = "disabled")
CT_disb_button.grid(row=CTButtonRow+3, column=CTButtonColumn, rowspan=2, padx=buttonPadX, pady=buttonPadY, sticky="w")

# Create game mode buttons
def GM_1():
    ser.write(b'M')
    print('Sent GM1 command')


GM1_button = ttk.Button(GM_frame, text="Mode 1", command=GM_1, style ="GreenRes.TButton", state = "disabled")
GM1_button.grid(row=GMButtonRow+1, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_2():
    ser.write(b'N')
    print('Sent GM2 command')


GM2_button = ttk.Button(GM_frame, text="Mode 2", command=GM_2, style ="GreenRes.TButton", state = "disabled")
GM2_button.grid(row=GMButtonRow+2, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_3():
    ser.write(b'O')
    print('Sent GM3 command')


GM3_button = ttk.Button(GM_frame, text="Mode 3", command=GM_3, style ="GreenRes.TButton", state = "disabled")
GM3_button.grid(row=GMButtonRow+3, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_4():
    ser.write(b'P')
    print('Sent GM4 command')


GM4_button = ttk.Button(GM_frame, text="Mode 4", command=GM_4, style ="GreenRes.TButton", state = "disabled")
GM4_button.grid(row=GMButtonRow+4, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_5():
    ser.write(b'Q')
    print('Sent GM5 command')


GM5_button = ttk.Button(GM_frame, text="Mode 5", command=GM_5, style ="GreenRes.TButton", state = "disabled")
GM5_button.grid(row=GMButtonRow+5, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")



# Create radio buttons to control Arduino pins
pin_var = tk.IntVar()

def update_pin(name, index, mode):
    pin = pin_var.get()
    if pin == 4:
        ser.write(b'0')
    elif pin == 5:
        ser.write(b'1')
    elif pin == 6:
        ser.write(b'2')
    elif pin == 7:
        ser.write(b'3')
    elif pin == 8:
        ser.write(b'4')
    elif pin == 12:
        ser.write(b'5')

pin_var.trace('w', update_pin)

# Create the actual radio buttons for spin speed and place them in the correct places
pin4_button = tk.Radiobutton(text="0%", variable=pin_var, value=4)
pin5_button = tk.Radiobutton(text="20%", variable=pin_var, value=5)
pin6_button = tk.Radiobutton(text="40%", variable=pin_var, value=6)
pin7_button = tk.Radiobutton(text="60%", variable=pin_var, value=7)
pin8_button = tk.Radiobutton(text="80%", variable=pin_var, value=8)
pin12_button = tk.Radiobutton(text="100%", variable=pin_var, value=12)


# Line up the radio buttons in the first column, with one button per row
pin4_button.grid(row=radioButtonRow+1, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin5_button.grid(row=radioButtonRow+2, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin6_button.grid(row=radioButtonRow+3, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin7_button.grid(row=radioButtonRow+4, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin8_button.grid(row=radioButtonRow+5, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin12_button.grid(row=radioButtonRow+6, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")

# Label the spin speed column
spinSpeedLabel = tk.Label(text="Spin Speed")
spinSpeedLabel.grid(row=radioButtonRow, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="nsew")

# Label the corner trap column
CTLabel = tk.Label(text="Corner Trap")
CTLabel.grid(row=CTButtonRow, column=CTButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="nsew")

# Label the game mode column
GMLabel = tk.Label(GM_frame, text="Game Mode")
GMLabel.grid(row=GMButtonRow, column=GMButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="nsew")


# Close serial port when window is closed
def on_closing():
    ser.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()