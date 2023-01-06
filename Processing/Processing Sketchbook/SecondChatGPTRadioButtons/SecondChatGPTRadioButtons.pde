import processing.serial.*;
import controlP5.*;

ControlP5 cp5;
Serial port;

void setup() {
  size(150, 200);
  cp5 = new ControlP5(this);

  // Set up the ON/OFF buttons
  cp5.addButton("onButton")
     .setPosition(10, 10)
     .setSize(40, 40)
     .setLabel("ON");
  cp5.addButton("offButton")
     .setPosition(50, 10)
     .setSize(40, 40)
     .setLabel("OFF");

  // Set up the radio buttons
  cp5.addRadio("colorRadio")
     .setPosition(10, 60)
     .setSize(80, 20)
     .setColorForeground(color(120))
     .setColorActive(color(255))
     .setColorLabel(color(255))
     .setItemsPerRow(1)
     .setSpacingColumn(50)
     .addItem("redRadio", 1)
     .addItem("greenRadio", 2)
     .addItem("blueRadio", 3)
     .addItem("yellowRadio", 4)
     .addItem("whiteRadio", 5)
     .activate(1);

  // Set up the serial port
  port = new Serial(this, "COM3", 9600);
  port.bufferUntil('\n');
}

void draw() {
  // Update the radio buttons
  Radio colorRadio = cp5.get(Radio.class, "colorRadio");
  if (colorRadio != null) {
    float selectedColorIndex = colorRadio.getValue();
    String colorLabel = colorRadio.getItem((int)selectedColorIndex).getName();
    if (colorLabel.equals("redRadio")) {
      fill(255, 0, 0);  // Set the fill color to red
      background(255, 0, 0);  // Set the background color to red
    }
    if (colorLabel.equals("greenRadio")) {
      fill(0, 255, 0);  // Set the fill color to green
      background(0, 255, 0);  // Set the background color to green
    }
    if (colorLabel.equals("blueRadio")) {
      fill(0, 0, 255);  // Set the fill color to blue
      background(0, 0, 255);  // Set the background color to blue
    }
    if (colorLabel.equals("yellowRadio")) {
      fill(255, 255, 0);  // Set the fill color to yellow
      background(255, 255, 0);  // Set the background color to yellow
    }
    if (colorLabel.equals("whiteRadio")) {
      fill(255, 255, 255);  // Set the fill color to white
      background(255, 255, 255);  // Set the background color to white
    }
    ellipse(50, 125, 10, 10);  // Draw the radio button indicator

    // Output the selected radio button number to the serial port
    println((int)selectedColorIndex);
    port.write((int)selectedColorIndex);
  }
}


void onButton() {
  port.write("1");  // Send the "ON" command to the Arduino
  println("ON");  // Print "ON" to the serial monitor
}

void offButton() {
  port.write("0");  // Send the "OFF" command to the Arduino
  println("OFF");  // Print "OFF" to the serial monitor
}

void serialEvent(Serial port) {
  // This function is called when new data is available from the serial port
  String data = port.readStringUntil('\n');  // Read the serial data
  println(data);  // Print the serial data to the serial monitor
}
