# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:09:33 2023

@author: Matt Dunbobbin
"""

import tkinter as tk
from tkinter import ttk
import serial
import GUIStyles
import subprocess
import os
import serial.tools.list_ports

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600)
ser.reset_input_buffer()

# Create main window
window = tk.Tk()
window.title("Arduino Control")

# Call in the created styles
GUIStyles.create_styles()



##############################################################################

# 'New' button in File menu in toolbar
def on_file_new():
    print("File > New clicked")

# 'Options' button in Tools menu in toolbar
def on_tools_options():
    print("Tools > Options clicked")

# 'About' button in Help menu in toolbar
def on_help_about():
    print("Help > About clicked")
    pdf_path = os.path.abspath(r"C:\Users\Matt\Documents\GitHub\ArenaControlMattD\Python\ArenaGUIHELP.pdf")
    subprocess.Popen(["start", pdf_path], shell=True)

# Allows the selection of COM ports
def on_com_select(com):
    try:
        ser.close()
    except serial.SerialException as e:
        print(f'Error closing port: {e}')
    ser.port = com
    ser.open()
    if ser.is_open:
        print(f'{com} is open')
    else:
        print(f'could not open {com}')
    
# Close serial port when window is closed
def on_closing():
    ser.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

##############################################################################

# Create a menu bar
menubar = tk.Menu(window)
window.config(menu=menubar)
    
# Create the File menu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_file_new)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_closing)

# Create the Tools menu
tools_menu = tk.Menu(menubar)
menubar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Options", command=on_tools_options)

# Create the COM port submenu
com_menu = tk.Menu(tools_menu)
tools_menu.add_cascade(label="Select COM port", menu=com_menu)

# Get the list of available COM ports
ports = list(serial.tools.list_ports.comports())

# Add the COM ports to the submenu
for port in ports:
    com_menu.add_radiobutton(label=port.device, command=lambda: on_com_select(port.device))
  

# Create the Help menu
help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=on_help_about)

##############################################################################

# Colours used in the seperate sections
SPINCOLOUR = 'pink'
CTCOLOUR = 'green'
GMCOLOUR = 'yellow'

# Set up padding and location varaibles
RADIOBUTTONSBUTTONX = 10
RADIOBUTTONSBUTTONY = 5
BUTTONPADX = 10
BUTTONPADY = 1
FRAMEPAD = 2
RADIOBUTTONCOLUMN = 0   #spin button locations
RADIOBUTTONROW = 2
CTBUTTONCOLUMN = 1  #Corner Trap button locations
CTBUTTONROW = 2
GMBUTTONCOLUMN = 2  #Game Mode button locations
GMBUTTONROW = 2

# Create a boarder around the spin speed radio buttons
spin_frame = tk.Frame(window, bg=SPINCOLOUR, bd=1, relief='solid')
spin_frame.grid(row=RADIOBUTTONROW, column=RADIOBUTTONCOLUMN, rowspan=7, padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')

# Create a boarder around the corner trap buttons
CT_frame = tk.Frame(window, bg=CTCOLOUR, bd=1, relief='solid')
CT_frame.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN, rowspan=3, padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')

# Create a boarder around the game mode buttons
GM_frame = tk.Frame(window, bg=GMCOLOUR, bd=1, relief='solid')
GM_frame.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN, rowspan=7, padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')

##############################################################################

# Create emergency stop button
def emergency_stop():
    ser.write(b'E') #sends recognizeable char to arduino
    ser.readline().decode().strip() #clears serial buffer after sending
    print('Sent emergency stop command')    #prints info for debug
    stop_button.state(["disabled"]) #disables the emergency stop button
    resume_button.state(["!disabled"])  #enables resume button
    
    #disables all other control buttons whilst in emergency stop mode
    pin4_button.config(state='disabled')
    pin5_button.config(state='disabled')
    pin6_button.config(state='disabled')
    pin7_button.config(state='disabled')
    pin8_button.config(state='disabled')
    pin12_button.config(state='disabled')
    CT_enb_button.config(state='disabled')
    CT_disb_button.config(state='disabled')
    GM1_button.config(state='disabled')
    GM2_button.config(state='disabled')
    GM3_button.config(state='disabled')
    GM4_button.config(state='disabled')
    GM5_button.config(state='disabled')
    window.after(100, update_con_label) #updates the status in GUI
    

stop_button = ttk.Button(window, text="Emergency Stop", command=emergency_stop, style ='RedEmerg.TButton')
stop_button.grid(row=0, column=0, columnspan = 3, padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")

# Create resume button
def resume():
    ser.write(b'R')
    ser.readline().decode().strip()
    print('Sent resume command')
    stop_button.state(["!disabled"])
    resume_button.state(["disabled"])
    pin4_button.config(state='normal')
    pin5_button.config(state='normal')
    pin6_button.config(state='normal')
    pin7_button.config(state='normal')
    pin8_button.config(state='normal')
    pin12_button.config(state='normal')
    CT_enb_button.config(state='normal')
    CT_disb_button.config(state='normal')
    GM1_button.config(state='normal')
    GM2_button.config(state='normal')
    GM3_button.config(state='normal')
    GM4_button.config(state='normal')
    GM5_button.config(state='normal')
    window.after(100, update_con_label)


resume_button = ttk.Button(window, text="Resume", command=resume, style ="GreenRes.TButton", state = "disabled")
resume_button.grid(row=1, column=0, columnspan = 3, padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")

##############################################################################

# Create corner trap enable button
def CT_enb():
    ser.write(b'C')
    print('Sent lower corner trap command')
    CT_enb_button.state(["disabled"])
    CT_disb_button.state(["!disabled"])


CT_enb_button = ttk.Button(CT_frame, text="LOWER", command=CT_enb, style ="CTStyle.TButton")
CT_enb_button.grid(row=CTBUTTONROW+1, column=CTBUTTONCOLUMN, rowspan=2, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

# Create corner trap disable button
def CT_disb():
    ser.write(b'D')
    print('Sent raise corner trap command')
    CT_enb_button.state(["!disabled"])
    CT_disb_button.state(["disabled"])

CT_disb_button = ttk.Button(CT_frame, text="RAISE", command=CT_disb, style ="CTStyle.TButton", state = "disabled")
CT_disb_button.grid(row=CTBUTTONROW+3, column=CTBUTTONCOLUMN, rowspan=2, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

##############################################################################

# Create game mode buttons
def GM_1():
    ser.write(b'M')
    print('Sent GM1 command')


GM1_button = ttk.Button(GM_frame, text="Mode 1", command=GM_1, style ="GM1Style.TButton", state = "normal")
GM1_button.grid(row=GMBUTTONROW+1, column=GMBUTTONCOLUMN, rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

def GM_2():
    ser.write(b'N')
    print('Sent GM2 command')


GM2_button = ttk.Button(GM_frame, text="Mode 2", command=GM_2, style ="GM2Style.TButton", state = "normal")
GM2_button.grid(row=GMBUTTONROW+2, column=GMBUTTONCOLUMN, rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

def GM_3():
    ser.write(b'O')
    print('Sent GM3 command')


GM3_button = ttk.Button(GM_frame, text="Mode 3", command=GM_3, style ="GM3Style.TButton", state = "normal")
GM3_button.grid(row=GMBUTTONROW+3, column=GMBUTTONCOLUMN, rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

def GM_4():
    ser.write(b'P')
    print('Sent GM4 command')


GM4_button = ttk.Button(GM_frame, text="Mode 4", command=GM_4, style ="GM4Style.TButton", state = "normal")
GM4_button.grid(row=GMBUTTONROW+4, column=GMBUTTONCOLUMN, rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

def GM_5():
    ser.write(b'Q')
    print('Sent GM5 command')


GM5_button = ttk.Button(GM_frame, text="Mode 5", command=GM_5, style ="GM5Style.TButton", state = "normal")
GM5_button.grid(row=GMBUTTONROW+5, column=GMBUTTONCOLUMN, rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

##############################################################################

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
pin4_button = tk.Radiobutton(spin_frame, text="0%", bg=SPINCOLOUR, variable=pin_var, value=4)
pin5_button = tk.Radiobutton(spin_frame, text="20%", bg=SPINCOLOUR, variable=pin_var, value=5)
pin6_button = tk.Radiobutton(spin_frame, text="40%", bg=SPINCOLOUR, variable=pin_var, value=6)
pin7_button = tk.Radiobutton(spin_frame, text="60%", bg=SPINCOLOUR, variable=pin_var, value=7)
pin8_button = tk.Radiobutton(spin_frame, text="80%", bg=SPINCOLOUR, variable=pin_var, value=8)
pin12_button = tk.Radiobutton(spin_frame, text="100%", bg=SPINCOLOUR, variable=pin_var, value=12)


# Line up the radio buttons in the first column, with one button per row
pin4_button.grid(row=RADIOBUTTONROW+1, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin5_button.grid(row=RADIOBUTTONROW+2, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin6_button.grid(row=RADIOBUTTONROW+3, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin7_button.grid(row=RADIOBUTTONROW+4, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin8_button.grid(row=RADIOBUTTONROW+5, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin12_button.grid(row=RADIOBUTTONROW+6, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")

##############################################################################

def update_con_label():
    # Read data from the serial port
    data = ser.readline().decode().strip()
    print(data)
    # Update the label with the new data
    data_label.config(text=data)
    # Call this function again after 100ms
    #window.after(100, update_con_label)
    
# Create a label to display the serial data
data_label = tk.Label(window, text="Waiting for serial data...")
data_label.grid(row=8, column=1)

##############################################################################

# Label the spin speed column
spinSpeedLabel = tk.Label(spin_frame, text="Spin Speed", bg=SPINCOLOUR)
spinSpeedLabel.grid(row=RADIOBUTTONROW, column=RADIOBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

# Label the corner trap column
CTLabel = tk.Label(CT_frame, text="Corner Trap", bg=CTCOLOUR)
CTLabel.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

# Label the game mode column
GMLabel = tk.Label(GM_frame, text="Game Mode", bg=GMCOLOUR)
GMLabel.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN, padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")




window.after(100, update_con_label)
window.mainloop()