# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 20:09:33 2023

@author: Matt Dunbobbin
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import os
import serial
import serial.tools.list_ports
import GUIStyles

# Set up serial communication with Arduino
ser = serial.Serial('COM3', 9600)
ser.reset_input_buffer()



# Create main window
window = tk.Tk()
window.title("Arduino Control")

# Call in the created styles
GUIStyles.create_styles()


##############################################################################


def on_file_new():
    """Create the 'New' button in File menu in toolbar"""
    print("File > New clicked")

def on_tools_options():
    """Create the 'Options' button in Tools menu in toolbar"""
    print("Tools > Options clicked")

def on_help_about():
    """Create the 'About' button in Help menu in toolbar"""
    print("Help > About clicked")
    pdf_path = os.path.abspath(r"C:\Users\Matt\Documents\GitHub\ArenaControlMattD\Python\ArenaGUIHELP.pdf")
    with open(pdf_path, "rb") as pdf_file:
        subprocess.Popen(["start", pdf_file.name], shell=True)

def on_com_select(com):
    """Allows the selection of COM ports in a drop down list"""
    try:
        ser.close()
    except serial.SerialException as exc:
        print(f'Error closing port: {exc}')
    ser.port = com
    ser.open()
    if ser.is_open:
        print(f'{com} is open')
    else:
        print(f'could not open {com}')

def on_closing():
    """Close serial port when window is closed"""
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
    com_menu.add_radiobutton(
        label=port.device, command=lambda: on_com_select(port.device))


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
RADIOBUTTONCOLUMN = 0  # spin button locations
RADIOBUTTONROW = 2
CTBUTTONCOLUMN = 1  # Corner Trap button locations
CTBUTTONROW = 2
GMBUTTONCOLUMN = 2  # Game Mode button locations
GMBUTTONROW = 2

ctbuttonEnbState = "!disabled"  # tracks state of corner trap buttons
ctbuttonDisbState = "disabled"


# Create a boarder around the spin speed radio buttons
spin_frame = tk.Frame(window, bg=SPINCOLOUR, bd=1, relief='solid')
spin_frame.grid(row=RADIOBUTTONROW, column=RADIOBUTTONCOLUMN,
                rowspan=7, padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')

# Create a boarder around the corner trap buttons
ct_frame = tk.Frame(window, bg=CTCOLOUR, bd=1, relief='solid')
ct_frame.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN, rowspan=3,
              padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')

# Create a boarder around the game mode buttons
gm_frame = tk.Frame(window, bg=GMCOLOUR, bd=1, relief='solid')
gm_frame.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN, rowspan=7,
              padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')

##############################################################################

# Create emergency stop button
def emergency_stop():
    """handles all procedures relating to emergency stop from GUI"""
    ser.write(b'E')  # sends recognizeable char to arduino
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent emergency stop command')  # prints info for debug
    stop_button.state(["disabled"])  # disables the emergency stop button
    resume_button.state(["!disabled"])  # enables resume button

    # disables all other control buttons whilst in emergency stop mode
    pin4_button.config(state='disabled')
    pin5_button.config(state='disabled')
    pin6_button.config(state='disabled')
    pin7_button.config(state='disabled')
    pin8_button.config(state='disabled')
    pin12_button.config(state='disabled')
    ct_enb_button.config(state='disabled')
    ct_disb_button.config(state='disabled')
    gm1_button.config(state='disabled')
    gm2_button.config(state='disabled')
    gm3_button.config(state='disabled')
    gm4_button.config(state='disabled')
    gm5_button.config(state='disabled')
    window.after(100, update_con_label)  # updates the status in GUI


stop_button = ttk.Button(window, text="Emergency Stop",
                         command=emergency_stop, style='RedEmerg.TButton')
stop_button.grid(row=0, column=0, columnspan=3,
                 padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")

# Create resume button
def resume():
    """handles all procedures relating to resuming from GUI"""
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
    ct_enb_button.config(state=ctbuttonEnbState)
    ct_disb_button.config(state=ctbuttonDisbState)
    gm1_button.config(state='normal')
    gm2_button.config(state='normal')
    gm3_button.config(state='normal')
    gm4_button.config(state='normal')
    gm5_button.config(state='normal')

    window.after(100, update_con_label)


resume_button = ttk.Button(
    window, text="Resume", command=resume, style="GreenRes.TButton", state="disabled")
resume_button.grid(row=1, column=0, columnspan=3,
                   padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")

##############################################################################

# Create corner trap enable button
def ct_enb():
    """handles enabling the corner trap from GUI"""
    ser.write(b'C')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent lower corner trap command')

    global ctbuttonEnbState  # allows access to these variables outside
    global ctbuttonDisbState  # of this function

    ct_enb_button.state(["disabled"])
    ct_disb_button.state(["!disabled"])
    ctbuttonEnbState = "disabled"
    ctbuttonDisbState = "!disabled"
    
    window.after(100, update_con_label)  # updates the status in GUI


ct_enb_button = ttk.Button(ct_frame, text="LOWER",
                           command=ct_enb, style="CTStyle.TButton")
ct_enb_button.grid(row=CTBUTTONROW+1, column=CTBUTTONCOLUMN,
                   rowspan=2, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

# Create corner trap disable button
def ct_disb():
    """handles disabling the corner trap from GUI"""
    ser.write(b'D')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent raise corner trap command')

    global ctbuttonEnbState  # allows access to these variables outside
    global ctbuttonDisbState  # of this function

    ct_enb_button.state(["!disabled"])
    ct_disb_button.state(["disabled"])
    ctbuttonEnbState = "!disabled"
    ctbuttonDisbState = "disabled"
    
    window.after(100, update_con_label)  # updates the status in GUI


ct_disb_button = ttk.Button(
    ct_frame, text="RAISE", command=ct_disb, style="CTStyle.TButton", state="disabled")
ct_disb_button.grid(row=CTBUTTONROW+3, column=CTBUTTONCOLUMN,
                    rowspan=2, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

##############################################################################

# Create game mode buttons
def gm_1():
    """controls Game Mode 1 from GUI"""
    ser.write(b'M')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent GM1 command')
    window.after(100, update_con_label)  # updates the status in GUI


gm1_button = ttk.Button(gm_frame, text="Mode 1",
                        command=gm_1, style="GM1Style.TButton", state="normal")
gm1_button.grid(row=GMBUTTONROW+1, column=GMBUTTONCOLUMN,
                rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")


def gm_2():
    """controls Game Mode 2 from GUI"""
    ser.write(b'N')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent GM2 command')
    window.after(100, update_con_label)  # updates the status in GUI


gm2_button = ttk.Button(gm_frame, text="Mode 2",
                        command=gm_2, style="GM2Style.TButton", state="normal")
gm2_button.grid(row=GMBUTTONROW+2, column=GMBUTTONCOLUMN,
                rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")


def gm_3():
    """controls Game Mode 3 from GUI"""
    ser.write(b'O')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent GM3 command')
    window.after(100, update_con_label)  # updates the status in GUI


gm3_button = ttk.Button(gm_frame, text="Mode 3",
                        command=gm_3, style="GM3Style.TButton", state="normal")
gm3_button.grid(row=GMBUTTONROW+3, column=GMBUTTONCOLUMN,
                rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")


def gm_4():
    """controls Game Mode 4 from GUI"""
    ser.write(b'P')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent GM4 command')
    window.after(100, update_con_label)  # updates the status in GUI


gm4_button = ttk.Button(gm_frame, text="Mode 4",
                        command=gm_4, style="GM4Style.TButton", state="normal")
gm4_button.grid(row=GMBUTTONROW+4, column=GMBUTTONCOLUMN,
                rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")


def gm_5():
    """controls Game Mode 5 from GUI"""
    ser.write(b'Q')
    ser.readline().decode().strip()  # clears serial buffer after sending
    print('Sent GM5 command')
    window.after(100, update_con_label)  # updates the status in GUI


gm5_button = ttk.Button(gm_frame, text="Mode 5",
                        command=gm_5, style="GM5Style.TButton", state="normal")
gm5_button.grid(row=GMBUTTONROW+5, column=GMBUTTONCOLUMN,
                rowspan=1, padx=BUTTONPADX, pady=BUTTONPADY, sticky="w")

##############################################################################

# Create radio buttons to control Arduino pins
pin_var = tk.IntVar()


def update_pin(name, index, mode):
    """controls updating the radiobuttons in real time"""
    pin = pin_var.get()
    if pin == 4:
        ser.write(b'0')
        ser.readline().decode().strip()  # clears serial buffer after sending
        window.after(100, update_con_label)  # updates the status in GUI
    elif pin == 5:
        ser.write(b'1')
        ser.readline().decode().strip()  # clears serial buffer after sending
        window.after(100, update_con_label)  # updates the status in GUI
    elif pin == 6:
        ser.write(b'2')
        ser.readline().decode().strip()  # clears serial buffer after sending
        window.after(100, update_con_label)  # updates the status in GUI
    elif pin == 7:
        ser.write(b'3')
        ser.readline().decode().strip()  # clears serial buffer after sending
        window.after(100, update_con_label)  # updates the status in GUI
    elif pin == 8:
        ser.write(b'4')
        ser.readline().decode().strip()  # clears serial buffer after sending
        window.after(100, update_con_label)  # updates the status in GUI
    elif pin == 12:
        ser.write(b'5')
        ser.readline().decode().strip()  # clears serial buffer after sending
        window.after(100, update_con_label)  # updates the status in GUI


pin_var.trace('w', update_pin)

# Create the actual radio buttons for spin speed and place them in the correct places
pin4_button = tk.Radiobutton(
    spin_frame, text="0%", bg=SPINCOLOUR, variable=pin_var, value=4)
pin5_button = tk.Radiobutton(
    spin_frame, text="20%", bg=SPINCOLOUR, variable=pin_var, value=5)
pin6_button = tk.Radiobutton(
    spin_frame, text="40%", bg=SPINCOLOUR, variable=pin_var, value=6)
pin7_button = tk.Radiobutton(
    spin_frame, text="60%", bg=SPINCOLOUR, variable=pin_var, value=7)
pin8_button = tk.Radiobutton(
    spin_frame, text="80%", bg=SPINCOLOUR, variable=pin_var, value=8)
pin12_button = tk.Radiobutton(
    spin_frame, text="100%", bg=SPINCOLOUR, variable=pin_var, value=12)



# Line up the radio buttons in the first column, with one button per row
pin4_button.grid(row=RADIOBUTTONROW+1, column=RADIOBUTTONCOLUMN,
                 padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin5_button.grid(row=RADIOBUTTONROW+2, column=RADIOBUTTONCOLUMN,
                 padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin6_button.grid(row=RADIOBUTTONROW+3, column=RADIOBUTTONCOLUMN,
                 padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin7_button.grid(row=RADIOBUTTONROW+4, column=RADIOBUTTONCOLUMN,
                 padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin8_button.grid(row=RADIOBUTTONROW+5, column=RADIOBUTTONCOLUMN,
                 padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")
pin12_button.grid(row=RADIOBUTTONROW+6, column=RADIOBUTTONCOLUMN,
                  padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="w")

##############################################################################


def update_con_label():
    """Updates the label reporting serial info from COM Port"""
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
spinSpeedLabel.grid(row=RADIOBUTTONROW, column=RADIOBUTTONCOLUMN,
                    padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

# Label the corner trap column
ctLabel = tk.Label(ct_frame, text="Corner Trap", bg=CTCOLOUR)
ctLabel.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN,
             padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

# Label the game mode column
gmLabel = tk.Label(gm_frame, text="Game Mode", bg=GMCOLOUR)
gmLabel.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN,
             padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")


window.after(100, update_con_label)
window.mainloop()
