# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 01:55:29 2023

@author: Matt Dunbobbin
"""
import tkinter as tk

def on_file_new():
    print("File > New clicked")

def on_tools_options():
    print("Tools > Options clicked")

def on_help_about():
    print("Help > About clicked")
    # Close serial port when window is closed
    
def on_closing():
    ser.close()
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)


# Create a menu bar
def createMenuBar(window):
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
    
    # Create the Help menu
    help_menu = tk.Menu(menubar)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=on_help_about)