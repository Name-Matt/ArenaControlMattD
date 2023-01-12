import tkinter as tk
import serial.tools.list_ports

def on_file_new():
    print("File > New clicked")

def on_tools_options():
    print("Tools > Options clicked")

def on_com_select(com):
    print(f"COM port selected: {com}")

root = tk.Tk()

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create the File menu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=on_file_new)
file_menu.add_command(label="Exit", command=root.quit)

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
    
root.mainloop()
