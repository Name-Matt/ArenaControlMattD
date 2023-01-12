# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 01:20:56 2023

@author: Matt Dunbobbin
"""
import tkinter.ttk as ttk

# Create styles used for buttons
def create_styles():
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
