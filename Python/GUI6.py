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

# Create styles used for buttons
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
CTButtonStyle = ttk.Style()
CTButtonStyle.theme_use('classic')
CTButtonStyle.configure('CTStyle.TButton', background = 'purple', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
CTButtonStyle.map('CTStyle.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'black')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', 'purple')])
GM1ButtonStyle = ttk.Style()
GM1ButtonStyle.theme_use('classic')
GM1ButtonStyle.configure('GM1Style.TButton', background = '#F0A150', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
GM1ButtonStyle.map('GM1Style.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', '#F0A150')])
GM2ButtonStyle = ttk.Style()
GM2ButtonStyle.theme_use('classic')
GM2ButtonStyle.configure('GM2Style.TButton', background = '#F09537', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
GM2ButtonStyle.map('GM2Style.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', '#F09537')])
GM3ButtonStyle = ttk.Style()
GM3ButtonStyle.theme_use('classic')
GM3ButtonStyle.configure('GM3Style.TButton', background = '#F48020', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
GM3ButtonStyle.map('GM3Style.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', '#F48020')])
GM4ButtonStyle = ttk.Style()
GM4ButtonStyle.theme_use('classic')
GM4ButtonStyle.configure('GM4Style.TButton', background = '#F0750F', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
GM4ButtonStyle.map('GM4Style.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', '#F5750F')])
GM5ButtonStyle = ttk.Style()
GM5ButtonStyle.theme_use('classic')
GM5ButtonStyle.configure('GM5Style.TButton', background = '#C76706', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
GM5ButtonStyle.map('GM5Style.TButton', foreground=[('disabled', 'black'),
                                                  ('pressed', 'pink'),
                                                  ('active', 'white')],
                                      background=[('disabled', 'grey'),
                                                  ('pressed', '!focus', 'cyan'),
                                                  ('active', '#C76706')])

# Colours used in the seperate sections
spinColour = 'pink'
CTColour = 'green'
GMColour = 'blue'

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
spin_frame = tk.Frame(window, bg=spinColour, bd=1, relief='solid')
spin_frame.grid(row=radioButtonRow, column=radioButtonColumn, rowspan=7, padx=framePad, pady=framePad, sticky='nsew')

# Create a boarder around the corner trap buttons
CT_frame = tk.Frame(window, bg=CTColour, bd=1, relief='solid')
CT_frame.grid(row=CTButtonRow, column=CTButtonColumn, rowspan=3, padx=framePad, pady=framePad, sticky='nsew')

# Create a boarder around the game mode buttons
GM_frame = tk.Frame(window, bg=GMColour, bd=1, relief='solid')
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
    print('Sent lower corner trap command')
    CT_enb_button.state(["disabled"])
    CT_disb_button.state(["!disabled"])


CT_enb_button = ttk.Button(CT_frame, text="LOWER", command=CT_enb, style ="CTStyle.TButton")
CT_enb_button.grid(row=CTButtonRow+1, column=CTButtonColumn, rowspan=2, padx=buttonPadX, pady=buttonPadY, sticky="w")

# Create corner trap disable button
def CT_disb():
    ser.write(b'D')
    print('Sent raise corner trap command')
    CT_enb_button.state(["!disabled"])
    CT_disb_button.state(["disabled"])

CT_disb_button = ttk.Button(CT_frame, text="RAISE", command=CT_disb, style ="CTStyle.TButton", state = "disabled")
CT_disb_button.grid(row=CTButtonRow+3, column=CTButtonColumn, rowspan=2, padx=buttonPadX, pady=buttonPadY, sticky="w")

# Create game mode buttons
def GM_1():
    ser.write(b'M')
    print('Sent GM1 command')


GM1_button = ttk.Button(GM_frame, text="Mode 1", command=GM_1, style ="GM1Style.TButton", state = "normal")
GM1_button.grid(row=GMButtonRow+1, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_2():
    ser.write(b'N')
    print('Sent GM2 command')


GM2_button = ttk.Button(GM_frame, text="Mode 2", command=GM_2, style ="GM2Style.TButton", state = "normal")
GM2_button.grid(row=GMButtonRow+2, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_3():
    ser.write(b'O')
    print('Sent GM3 command')


GM3_button = ttk.Button(GM_frame, text="Mode 3", command=GM_3, style ="GM3Style.TButton", state = "normal")
GM3_button.grid(row=GMButtonRow+3, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_4():
    ser.write(b'P')
    print('Sent GM4 command')


GM4_button = ttk.Button(GM_frame, text="Mode 4", command=GM_4, style ="GM4Style.TButton", state = "normal")
GM4_button.grid(row=GMButtonRow+4, column=GMButtonColumn, rowspan=1, padx=buttonPadX, pady=buttonPadY, sticky="w")

def GM_5():
    ser.write(b'Q')
    print('Sent GM5 command')


GM5_button = ttk.Button(GM_frame, text="Mode 5", command=GM_5, style ="GM5Style.TButton", state = "normal")
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
pin4_button = tk.Radiobutton(spin_frame, text="0%", bg=spinColour, variable=pin_var, value=4)
pin5_button = tk.Radiobutton(spin_frame, text="20%", bg=spinColour, variable=pin_var, value=5)
pin6_button = tk.Radiobutton(spin_frame, text="40%", bg=spinColour, variable=pin_var, value=6)
pin7_button = tk.Radiobutton(spin_frame, text="60%", bg=spinColour, variable=pin_var, value=7)
pin8_button = tk.Radiobutton(spin_frame, text="80%", bg=spinColour, variable=pin_var, value=8)
pin12_button = tk.Radiobutton(spin_frame, text="100%", bg=spinColour, variable=pin_var, value=12)


# Line up the radio buttons in the first column, with one button per row
pin4_button.grid(row=radioButtonRow+1, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin5_button.grid(row=radioButtonRow+2, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin6_button.grid(row=radioButtonRow+3, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin7_button.grid(row=radioButtonRow+4, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin8_button.grid(row=radioButtonRow+5, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")
pin12_button.grid(row=radioButtonRow+6, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="w")

# Label the spin speed column
spinSpeedLabel = tk.Label(spin_frame, text="Spin Speed", bg=spinColour)
spinSpeedLabel.grid(row=radioButtonRow, column=radioButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="nsew")

# Label the corner trap column
CTLabel = tk.Label(CT_frame, text="Corner Trap", bg=CTColour)
CTLabel.grid(row=CTButtonRow, column=CTButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="nsew")

# Label the game mode column
GMLabel = tk.Label(GM_frame, text="Game Mode", bg=GMColour, fg='white')
GMLabel.grid(row=GMButtonRow, column=GMButtonColumn, padx=radioButtonsPadX, pady=radioButtonsPadY, sticky="nsew")


# Close serial port when window is closed
def on_closing():
    ser.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()