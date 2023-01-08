import serial
import time
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up the serial connection to the Arduino
        self.serial_port = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)  # Give the Arduino time to reset

        # Create the button for emergency stop
        self.emergency_stop_button = QtWidgets.QPushButton('Emergency Stop')
        self.emergency_stop_button.setStyleSheet('color: red')
        self.emergency_stop_button.clicked.connect(self.emergency_stop)

        # Create the radio buttons for controlling the Arduino pins
        self.pin4_button = QtWidgets.QRadioButton('Pin 4')
        self.pin4_button.toggled.connect(lambda: self.set_pin(4, self.pin4_button.isChecked()))
        self.pin5_button = QtWidgets.QRadioButton('Pin 5')
        self.pin5_button.toggled.connect(lambda: self.set_pin(5, self.pin5_button.isChecked()))
        self.pin6_button = QtWidgets.QRadioButton('Pin 6')
        self.pin6_button.toggled.connect(lambda: self.set_pin(6, self.pin6_button.isChecked()))
        self.pin7_button = QtWidgets.QRadioButton('Pin 7')
        self.pin7_button.toggled.connect(lambda: self.set_pin(7, self.pin7_button.isChecked()))
        self.pin8_button = QtWidgets.QRadioButton('Pin 8')
        self.pin8_button.toggled.connect(lambda: self.set_pin(8, self.pin8_button.isChecked()))
        self.pin12_button = QtWidgets.QRadioButton('Pin 12')
        self.pin12_button.toggled.connect(lambda: self.set_pin(12, self.pin12_button.isChecked()))

        # Add the buttons to a horizontal layout
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.emergency_stop_button)
        button_layout.addWidget(self.pin4_button)
        button_layout.addWidget(self.pin5_button)
        button_layout.addWidget(self.pin6_button)
        button_layout.addWidget(self.pin7_button)
        button_layout.addWidget(self.pin8_button)
        button_layout.addWidget(self.pin12_button)

        # Add the layout to the central widget
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(button_layout)
        self.setCentralWidget(central_widget)

        # Set up a timer to update the radio buttons in real time
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update_buttons)
        self.update_timer.start(100)  # Update every 100 milliseconds

    def set_pin(self, pin, value):
        """Send a command to the Arduino to set a digital pin HIGH or LOW."""
        if value:
            self.serial_port.write(f'{pin}H'.encode())
        else:
            self.serial_port.write(f'{pin}L'.encode())

    def emergency_stop(self):
        """Send a command to the Arduino to set all pins LOW."""
        self.serial_port.write(b'S')
        self.pin4_button.setChecked(False)
        self.pin5_button.setChecked(False)
        self.pin6_button.setChecked(False)
        self.pin7_button.setChecked(False)
        self.pin8_button.setChecked(False)
        self.pin12_button.setChecked(False)

    def update_buttons(self):
        """Update the radio buttons to reflect the current state of the Arduino pins."""
        status = self.serial_port.readline().strip().decode()
        if status:
            self.pin4_button.setChecked('4' in status)
            self.pin5_button.setChecked('5' in status)
            self.pin6_button.setChecked('6' in status)
            self.pin7_button.setChecked('7' in status)
            self.pin8_button.setChecked('8' in status)
            self.pin12_button.setChecked('12' in status)
            
    def closeEvent(self, event):
        """Close the serial port when the window is closed."""
        self.serial_port.close()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

