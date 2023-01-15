import tkinter as tk
import serial
import threading

class ArduinoControl(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial("COM3", 9600)  # open serial port
        self.title("Arduino Control")
        self.stop_thread = tk.BooleanVar(value=False)
        # Emergency stop button
        self.stop_button = tk.Button(self, text="Emergency Stop", command=self.stop, bg = "red")
        self.stop_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.stop_button.config(height = 3, width = 15)

        # Resume button
        self.resume_button = tk.Button(self, text="Resume", command=self.resume, state="disable", bg = "green")
        self.resume_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.resume_button.config(height = 3, width = 15)

        # Percentage buttons
        self.percentage = tk.StringVar()
        self.percentage.set("0")
        self.percentage_buttons = []
        for i in range(6):
            button = tk.Radiobutton(self, text=str((i)*20) + "%", variable=self.percentage, value=str(i), command = self.set_percentage)
            self.percentage_buttons.append(button)
            button.grid(row=1, column=i)
            

        # Enable/disable buttons
        self.enable_button = tk.Button(self, text="Enable", command=self.enable)
        self.enable_button.grid(row=2, column=0, padx=10, pady=10)

        self.disable_button = tk.Button(self, text="Disable", command=self.disable)
        self.disable_button.grid(row=2, column=1, padx=10, pady=10)

        # Game mode buttons
        self.game_mode = tk.StringVar()
        self.game_mode_buttons = []
        for i in range(5):
            button = tk.Button(self, text="Mode " + str(i+1), command=lambda mode=chr(77+i): self.set_game_mode(mode), bg="white")
            self.game_mode_buttons.append(button)
            button.grid(row=3, column=i)
            
            
        # Text box for serial data
        self.serial_data = tk.Text(self, height=10, width=30)
        self.serial_data.grid(row=4, column=0, columnspan=5, padx=10, pady=10)
    
        # Create a thread for reading serial data
        self.thread = threading.Thread(target=self.update_serial_data)
        self.thread.start()
    
    def update_serial_data(self):
        """Read serial data and update the text box"""
        while not self.stop_thread.get():
            data = self.ser.readline().decode()
            self.serial_data.insert("end", data)
            self.serial_data.see("end")
            self.update()
    
    def stop(self):
        """Emergency stop button"""
        self.ser.write(b'E')
        self.resume_button.config(state="normal")
        for button in self.percentage_buttons + self.game_mode_buttons:
            button.config(state="disable")
        self.enable_button.config(state="disable")
        self.disable_button.config(state="disable")
    
    def resume(self):
        """Resume button"""
        self.ser.write(b'R')
        self.resume_button.config(state="disable")
        for button in self.percentage_buttons + self.game_mode_buttons:
            button.config(state="normal")
        self.enable_button.config(state="normal")
        self.disable_button.config(state="normal")
    
    def set_percentage(self):
        """Set the percentage level"""
        self.ser.write(self.percentage.get().encode())
    
    def enable(self):
        """Enable button"""
        self.ser.write(b'C')

    def disable(self):
        """Disable button"""
        self.ser.write(b'D')
    
    def set_game_mode(self, mode):
        """Set the game mode"""
        self.ser.write(mode.encode())

    def close(self):
        self.stop_thread.set(True)
        self.ser.close()
        super().destroy()


if __name__ == "__main__":
    app = ArduinoControl()
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()