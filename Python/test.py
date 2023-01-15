import tkinter as tk
import serial
import threading


class ArduinoControl(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial("COM3", 9600)  # open serial port
        self.title("Arduino Control")
        # flag to track state of thread
        self.stop_thread = tk.BooleanVar(value=False)
        
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
                        rowspan=8, padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')
        # Label the spin speed column
        self.spinSpeedLabel = tk.Label(self.spin_frame, text="Spin Speed", bg=SPINCOLOUR)
        self.spinSpeedLabel.grid(row=RADIOBUTTONROW+1, column=RADIOBUTTONCOLUMN,
                            padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

        # Create a boarder around the corner trap buttons
        self.ct_frame = tk.Frame(self, bg=CTCOLOUR, bd=1, relief='solid')
        self.ct_frame.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN, rowspan=8,
                      padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')
        # Label the corner trap column
        self.ctLabel = tk.Label(self.ct_frame, text="Corner Trap", bg=CTCOLOUR)
        self.ctLabel.grid(row=CTBUTTONROW, column=CTBUTTONCOLUMN,
                     padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")

        # Create a boarder around the game mode buttons
        self.gm_frame = tk.Frame(self, bg=GMCOLOUR, bd=1, relief='solid')
        self.gm_frame.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN, rowspan=8,
                      padx=FRAMEPAD, pady=FRAMEPAD, sticky='nsew')
        # Label the game mode column
        self.gmLabel = tk.Label(self.gm_frame, text="Game Mode", bg=GMCOLOUR)
        self.gmLabel.grid(row=GMBUTTONROW, column=GMBUTTONCOLUMN,
                     padx=RADIOBUTTONSBUTTONX, pady=RADIOBUTTONSBUTTONY, sticky="nsew")
        
        # Emergency stop button
        self.stop_button = tk.Button(
            self, text="Emergency Stop", command=self.stop, bg="red")
        self.stop_button.grid(row=0, column=0, columnspan=2,
                              padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")
        #self.stop_button.config(height=3, width=15)

        # Resume button
        self.resume_button = tk.Button(
            self, text="Resume", command=self.resume, state="disable", bg="green")
        self.resume_button.grid(
            row=0, column=3, columnspan=2, padx=BUTTONPADX, pady=BUTTONPADY, sticky="nsew")
        #self.resume_button.config(height=3, width=15)
        
        # Percentage buttons
        self.percentage = tk.StringVar()
        self.percentage.set("0")
        self.percentage_buttons = []
        for i in range(6):
            button = tk.Radiobutton(self, text=str(
                (i)*20) + "%", variable=self.percentage, value=str(i), command=self.set_percentage)
            self.percentage_buttons.append(button)
            button.grid(row=RADIOBUTTONROW+2+i, column=RADIOBUTTONCOLUMN, padx=10, pady=5)
            
    def set_percentage(self):
        """Set the percentage level"""
        self.ser.write(self.percentage.get().encode())
        
    def stop(self):
        """Emergency stop button"""
        self.ser.write(b'E')
        self.stop_button.config(state="disable")
        self.resume_button.config(state="normal")
        for button in self.percentage_buttons + self.game_mode_buttons:
            button.config(state="disable")
        self.enable_button.config(state="disable")
        self.disable_button.config(state="disable")
        
    def resume(self):
        """Resume button"""
        self.ser.write(b'R')
        self.stop_button.config(state="normal")
        self.resume_button.config(state="disable")
        for button in self.percentage_buttons + self.game_mode_buttons:
            button.config(state="normal")
        self.enable_button.config(state="normal")
        self.disable_button.config(state="normal")
        
    def close(self):
        self.stop_thread.set(True)
        self.ser.close()
        super().destroy()


if __name__ == "__main__":
    app = ArduinoControl()
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()
