import tkinter as tk
from tkinter import ttk
import serial
import threading

class ArduinoControl(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial("COM3", 9600)  # open serial port
        self.title("Arduino Control")

        # Emergency stop button
        self.stop_button = ttk.Button(self, text="Emergency Stop", command=self.stop)
        self.stop_button.grid(row=0, column=0, padx=10, pady=10)

        # Resume button
        self.resume_button = ttk.Button(self, text="Resume", command=self.resume, state="disable")
        self.resume_button.grid(row=0, column=1, padx=10, pady=10)

        # Percentage radio buttons
        self.percentage = tk.StringVar()
        self.percentage_buttons = []
        for i in range(6):
            button = ttk.Radiobutton(self, text=str(i*20) + "%", variable=self.percentage, value=str(i), command = self.set_percentage)
            self.percentage_buttons.append(button)
            button.grid(row=1, column=i)

        # Enable/disable button
        self.enable_var = tk.BooleanVar()
        self.enable_button = ttk.Checkbutton(self, text="Enable", variable=self.enable_var, command = self.enable)
        self.disable_button = ttk.Checkbutton(self, text="Disable", variable=self.enable_var, onvalue=False, command = self.disable)
        self.enable_button.grid(row=2, column=0)
        self.disable_button.grid(row=2, column=1)

        # Game mode buttons
        self.game_mode = tk.StringVar()
        self.game_mode_buttons = []
        for i in range(5):
            button = ttk.Radiobutton(self, text="Mode " + str(i+1), variable=self.game_mode, value=chr(77+i), command = self.set_game_mode)
            self.game_mode_buttons.append(button)
            button.grid(row=3, column=i)

        # Text box for serial data
        self.serial_data = tk.Text(self, height=10, width=30)
        self.serial_data.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

        # Create a thread for reading serial data
        self.thread = threading.Thread(target=self.update_serial_data)
        self.thread.start()

    def stop(self):
        self.ser.write(b"E")
        # Disable all buttons and widgets
        self.stop_button.config(state="disable")
        self.resume_button.config(state="normal")
        for button in self.percentage_buttons:
            button.config(state="disable")
        self.enable_button.config(state="disable")
        self.disable_button.config(state="disable")
        for button in self.game_mode_buttons:
            button.config(state="disable")
    def resume(self):
        self.ser.write(b"R")
        percentage = self.percentage.get()
        self.ser.write(percentage.encode())
        # Enable all buttons and widgets
        self.stop_button.config(state="normal")
        self.resume_button.config(state="disable")
        for button in self.percentage_buttons:
            button.config(state="normal")
        self.enable_button.config(state="normal")
        self.disable_button.config(state="normal")
        for button in self.game_mode_buttons:
            button.config(state="normal")
    def set_percentage(self):
        percentage = self.percentage.get()
        self.ser.write(percentage.encode())

    def enable(self):
        self.ser.write(b"C")

    def disable(self):
        self.ser.write(b"D")

    def set_game_mode(self):
        mode = self.game_mode.get()
        self.ser.write(mode.encode())

    def update_serial_data(self):
        """Read serial data and update the text box"""
        while True:
            data = self.ser.readline().decode()
            self.serial_data.insert("end", data)
            self.serial_data.see("end")
            self.update()
    def close(self):
        self.ser.close()
        super().destroy()

if __name__ == "__main__":
    app = ArduinoControl()
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()