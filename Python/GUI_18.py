import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import subprocess
import os
import threading
import serial
import serial.tools.list_ports
import GUIStyles as GS
# Open OBS
#os.system(r"""start /D "E:\OBSPortable" OBSPortable.exe""")


class ArduinoControl(tk.Tk):
    """creates an area for the window to exist"""
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial(None, 9600)

        self.iconbitmap(r'C:\Users\Matt\Downloads\uolcrest.ico')

        self.title("Arduino Control")
        # flag to track state of thread
        self.stop_thread = tk.BooleanVar(value=False)
        
        # Call in the created styles
        GS.create_styles()
        self.gm_but_styles = ['GM1Style.TButton','GM2Style.TButton','GM3Style.TButton','GM4Style.TButton','GM5Style.TButton']
        self.colour_but_styles = ['BLUEButtonStyle.TButton','GREENButtonStyle.TButton','PINKButtonStyle.TButton','YELLOWButtonStyle.TButton','FLASHButtonStyle.TButton']
        
        # Create list of different colour LED states
        self.LED_colours = ['Blue','Green','Pink','Yellow','5 Flash']

        # Create a menu bar
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
        
        # Create the File menu
        self.file_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.on_file_new)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.close)

        # Create the Tools menu
        self.tools_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Tools", menu=self.tools_menu)
        self.tools_menu.add_command(label="Options", command=self.on_tools_options)
        
        # Create the COM port submenu
        self.com_menu = tk.Menu(self.tools_menu)
        self.tools_menu.add_cascade(label="Select COM port", menu=self.com_menu)
        
        # Get the list of available COM ports
        self.ports = list(serial.tools.list_ports.comports())
        
        # Add the COM ports to the submenu
        for port in self.ports:
            self.com_menu.add_radiobutton(
                label=port.description, command=lambda: self.on_com_select(port.device))
        
        
        # Create the Help menu
        self.help_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.on_help_about)


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
        RADIOBUTTONROW = 1
        CTBUTTONCOLUMN = 2  # Corner Trap button locations
        CTBUTTONROW = 1
        GMBUTTONCOLUMN = 4  # Game Mode button locations
        GMBUTTONROW = 1

        # Create a boarder around the spin speed radio buttons
        self.spin_frame = tk.Frame(self, bg=SPINCOLOUR, bd=1, relief='solid')
        self.spin_frame.grid(row=RADIOBUTTONROW, column=RADIOBUTTONCOLUMN,
                             padx=FRAMEPAD, pady=FRAMEPAD, columnspan=2, sticky='nsew')
        # Label the spin speed column
        self.spin_speed_label = tk.Label(
            self.spin_frame, text="Spin Speed", bg=SPINCOLOUR)
        self.spin_speed_label.grid(row=RADIOBUTTONROW, column=RADIOBUTTONCOLUMN,
                                 padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

        # Create a boarder around the corner trap buttons
        self.ct_frame = tk.Frame(self, bg=CTCOLOUR, bd=1, relief='solid')
        self.ct_frame.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN,
                           padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')
        # Label the corner trap column
        self.ct_label = tk.Label(self.ct_frame, text="Corner Trap", bg=CTCOLOUR)
        self.ct_label.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN,
                          padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

        # Create a boarder around the game mode buttons
        self.gm_frame = tk.Frame(self, bg=GMCOLOUR, bd=1, relief='solid')
        self.gm_frame.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN,
                           padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')
        # Label the game mode column
        self.gm_label = tk.Label(self.gm_frame, text="Game Mode", bg=GMCOLOUR)
        self.gm_label.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN,
                          padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

        # Emergency stop button
        self.stop_button = ttk.Button(self, text="Emergency Stop",
                                 command=self.stop, style='RedEmerg.TButton')
        self.stop_button.grid(row=0, column=0, columnspan=2,
                              padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")

        # Resume button
        self.resume_button = ttk.Button(
            self, text="Resume", command=self.resume, style="GreenRes.TButton", state="disabled")
        self.resume_button.grid(
            row=0, column=3, columnspan=2, padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")

        # Percentage buttons
        self.percentage = tk.StringVar()
        self.percentage.set("0")
        self.percentage_buttons = []
        for i in range(6):
            button = tk.Radiobutton(self.spin_frame, text=str(
                (i)*20) + "%", bg=SPINCOLOUR, variable=self.percentage, value=str(i), command=self.set_percentage)
            self.percentage_buttons.append(button)
            button.grid(row=(RADIOBUTTONROW+1)+i,
                        column=RADIOBUTTONCOLUMN, padx=10, pady=5)

        # Enable/disable buttons
        self.enable_button = ttk.Button(
           self.ct_frame, text="RAISE", command=self.enable, style="CTStyle.TButton", state="disabled")
        self.enable_button.grid(
            row=CTBUTTONROW+1, column=CTBUTTONCOLUMN, padx=10, pady=5)
        self.enable_button_state = "disabled"


        self.disable_button = ttk.Button(self.ct_frame, text="LOWER",
                                  command=self.disable, style="CTStyle.TButton")
        self.disable_button.grid(
            row=CTBUTTONROW+2, column=CTBUTTONCOLUMN, padx=10, pady=5)
        self.disable_button_state = "normal"

        # Game mode buttons
        self.game_mode = tk.StringVar()
        self.game_mode_buttons = []
        for i in range(5):
            button = ttk.Button(self.gm_frame, text=self.LED_colours[i],
                                    command=lambda mode=chr(77+i): self.set_game_mode(mode), style=self.colour_but_styles[i], state="normal")
            self.game_mode_buttons.append(button)
            button.grid(row=(GMBUTTONROW+1)+i,
                        column=GMBUTTONCOLUMN, padx=10, pady=5)
        

        # Text box for serial data
        self.serial_data = tk.Text(self, height=5, width=30)
        self.serial_data.grid(row=9, column=0, columnspan=5, padx=10, pady=10)
        


    def update_serial_data(self):
        """Read serial data and update the text box"""
        if self.ser != None:
            while not self.stop_thread.get():
                data = self.ser.readline().decode()
                self.serial_data.insert("end", data)
                self.serial_data.see("end")
                self.update()

    def stop(self):
        """Emergency stop button"""
        if self.ser.port == None:
            tk.messagebox.showerror("Serial Port Error", "Please check if the Arduino is connected and that the correct port is selected. Go Tools -> Select COM port")
        else:
            self.ser.write(b'E')    #the b means it is a byte string
            self.stop_button.config(state="disable")
            self.resume_button.config(state="normal")
            for button in self.percentage_buttons + self.game_mode_buttons:
                button.config(state="disable")
            self.enable_button.config(state="disable")
            self.disable_button.config(state="disable")

    def resume(self):
        """Resume button"""
        if self.ser.port == None:
            tk.messagebox.showerror("Serial Port Error", "Please check if the Arduino is connected and that the correct port is selected. Go Tools -> Select COM port")
        else:
            self.ser.write(b'R')
            self.stop_button.config(state="normal")
            self.resume_button.config(state="disable")
            for button in self.percentage_buttons + self.game_mode_buttons:
                button.config(state="normal")
            self.enable_button.config(state=self.enable_button_state)
            self.disable_button.config(state=self.disable_button_state)

    def set_percentage(self):
        """Set the percentage level"""
        if self.ser.port == None:
            tk.messagebox.showerror("Serial Port Error", "Please check if the Arduino is connected and that the correct port is selected. Go Tools -> Select COM port")
        else:
            self.ser.write(self.percentage.get().encode())

    def enable(self):
        """Enable button"""
        if self.ser.port == None:
            tk.messagebox.showerror("Serial Port Error", "Please check if the Arduino is connected and that the correct port is selected. Go Tools -> Select COM port")
        else:
            self.ser.write(b'C')
            self.enable_button.config(state="disable")
            self.disable_button.config(state="normal")
            self.enable_button_state = "disable"
            self.disable_button_state = "normal"

    def disable(self):
        """Disable button"""
        if self.ser.port == None:
            tk.messagebox.showerror("Serial Port Error", "Please check if the Arduino is connected and that the correct port is selected. Go Tools -> Select COM port")
        else:
            self.ser.write(b'D')
            self.disable_button.config(state="disable")
            self.enable_button.config(state="normal")
            self.disable_button_state = "disable"
            self.enable_button_state = "normal"

    def set_game_mode(self, mode):
        """Set the game mode"""
        if self.ser.port == None:
            tk.messagebox.showerror("Serial Port Error", "Please check if the Arduino is connected and that the correct port is selected. Go Tools -> Select COM port")
        else:
            self.ser.write(mode.encode())
        
    def on_file_new(self):
        """Create the 'New' button in File menu in toolbar"""
        print("File > New clicked")

    def on_tools_options(self):
        """Create the 'Options' button in Tools menu in toolbar"""
        print("Tools > Options clicked")

    def on_help_about(self):
        """Create the 'About' button in Help menu in toolbar"""
        print("Help > About clicked")
        pdf_path = os.path.abspath(r"C:\Users\Matt\Documents\GitHub\ArenaControlMattD\Python\ArenaGUIHELP.pdf")
        with open(pdf_path, "rb") as pdf_file:
            subprocess.Popen(["start", pdf_file.name], shell=True)

    def on_com_select(self, com):
        """Allows the selection of COM ports in a drop down list"""
        try:
            self.ser.close()
        except serial.SerialException as exc:
            print(f'Error closing port: {exc}')
        self.ser.port = com
        self.ser.open()
        
        # Create a thread for reading serial data
        self.thread = threading.Thread(target=self.update_serial_data)
        self.thread.start()
        
        if self.ser.is_open:
            print(f'{com} is open')
        else:
            print(f'could not open {com}')

    def close(self):
        """closes serial lines and the window"""
        #self.stop_thread.set(True)
        self.ser.close()
        super().destroy()


if __name__ == "__main__":
    app = ArduinoControl()
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()
