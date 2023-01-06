import processing.serial.*;  // Import the serial library

Serial port;  // Declare a variable to store the serial port

// Set up the button dimensions
int buttonWidth = 75;
int buttonHeight = 50;
int buttonPadding = 10;

// Set up the button positions
int onButtonX = 50;
int onButtonY = 50;
int offButtonX = 150;
int offButtonY = 50;

// Set up the radio button dimensions
int radioButtonSize = 20;
int radioButtonPadding = 10;

// Set up the radio button positions
int redRadioButtonX = 50;
int redRadioButtonY = 125;
int greenRadioButtonX = 100;
int greenRadioButtonY = 125;
int blueRadioButtonX = 150;
int blueRadioButtonY = 125;
int yellowRadioButtonX = 200;
int yellowRadioButtonY = 125;
int whiteRadioButtonX = 250;
int whiteRadioButtonY = 125;

// Set up the radio button state variables
boolean redRadioButtonState = false;
boolean greenRadioButtonState = false;
boolean blueRadioButtonState = false;
boolean yellowRadioButtonState = false;
boolean whiteRadioButtonState = false;

void setup() {
  size(300, 200);  // Set the size of the window
  background(255);  // Set the background color to white

  // Set up the serial port
  String portName = "COM3";  // Use the COM3 port
  port = new Serial(this, portName, 9600);  // Open the port at a baud rate of 9600
}

void draw() {
  // Draw the "ON" button
  fill(200);  // Set the fill color to light gray
  rect(onButtonX, onButtonY, buttonWidth, buttonHeight);  // Draw the button
  fill(0);  // Set the fill color to black
  textSize(16);  // Set the text size
  text("ON", onButtonX + buttonWidth / 2, onButtonY + buttonHeight / 2);  // Draw the button label

  // Draw the "OFF" button
  fill(200);  // Set the fill color to light gray
  rect(offButtonX, offButtonY, buttonWidth, buttonHeight);  // Draw the button
  fill(0);  // Set the fill color to black
  textSize(16);  // Set the text size
  text("OFF", offButtonX + buttonWidth / 2, offButtonY + buttonHeight / 2);  // Draw the button label

  // Draw the radio buttons
  fill(200);  // Set the fill color to light gray
  ellipse(redRadioButtonX, redRadioButtonY, radioButtonSize, radioButtonSize);  // Draw the red radio button
  ellipse(greenRadioButtonX, greenRadioButtonY, radioButtonSize, radioButtonSize);  // Draw the green radio button
  ellipse(blueRadioButtonX, blueRadioButtonY, radioButtonSize, radioButtonSize);  //Draw the blue radio button
  ellipse(yellowRadioButtonX, yellowRadioButtonY, radioButtonSize, radioButtonSize);  // Draw the yellow radio button
  ellipse(whiteRadioButtonX, whiteRadioButtonY, radioButtonSize, radioButtonSize);  // Draw the white radio button

  // Draw the radio button labels
  fill(0);  // Set the fill color to black
  textSize(16);  // Set the text size
  text("Red", redRadioButtonX + radioButtonSize + radioButtonPadding, redRadioButtonY + radioButtonSize / 2);  // Draw the red radio button label
  text("Green", greenRadioButtonX + radioButtonSize + radioButtonPadding, greenRadioButtonY + radioButtonSize / 2);  // Draw the green radio button label
  text("Blue", blueRadioButtonX + radioButtonSize + radioButtonPadding, blueRadioButtonY + radioButtonSize / 2);  // Draw the blue radio button label
  text("Yellow", yellowRadioButtonX + radioButtonSize + radioButtonPadding, yellowRadioButtonY + radioButtonSize / 2);  // Draw the yellow radio button label
  text("White", whiteRadioButtonX + radioButtonSize + radioButtonPadding, whiteRadioButtonY + radioButtonSize / 2);  // Draw the white radio button label

  // Update the radio button states
  if (mousePressed) {  // If the mouse is pressed
    // Check if the mouse is over one of the radio buttons
    if (dist(mouseX, mouseY, redRadioButtonX, redRadioButtonY) < radioButtonSize / 2) {
      redRadioButtonState = true;
      greenRadioButtonState = false;
      blueRadioButtonState = false;
      yellowRadioButtonState = false;
      whiteRadioButtonState = false;
    }
    if (dist(mouseX, mouseY, greenRadioButtonX, greenRadioButtonY) < radioButtonSize / 2) {
      redRadioButtonState = false;
      greenRadioButtonState = true;
      blueRadioButtonState = false;
      yellowRadioButtonState = false;
      whiteRadioButtonState = false;
    }
    if (dist(mouseX, mouseY, blueRadioButtonX, blueRadioButtonY) < radioButtonSize / 2) {
      redRadioButtonState = false;
      greenRadioButtonState = false;
      blueRadioButtonState = true;
      yellowRadioButtonState = false;
      whiteRadioButtonState = false;
    }
    if (dist(mouseX, mouseY, yellowRadioButtonX, yellowRadioButtonY) < radioButtonSize / 2) {
      redRadioButtonState = false;
      greenRadioButtonState = false;
      blueRadioButtonState = false;
      yellowRadioButtonState = true;
      whiteRadioButtonState = false;
    }
    if (dist(mouseX, mouseY, whiteRadioButtonX, whiteRadioButtonY) < radioButtonSize / 2) {
      redRadioButtonState = false;
      greenRadioButtonState = false;
      blueRadioButtonState = false;
      yellowRadioButtonState = false;
      whiteRadioButtonState = true;
    }
  }

  // Update the radio buttons
  if (redRadioButtonState) {
    fill(255, 0, 0);  // Set the fill colour to red
  }
  if (greenRadioButtonState) {
    fill(0, 255, 0);  // Set the fill color to green
  }
  if (blueRadioButtonState) {
    fill(0, 0, 255);  // Set the fill color to blue
  }
  if (yellowRadioButtonState) {
    fill(255, 255, 0);  // Set the fill color to yellow
  }
  if (whiteRadioButtonState) {
    fill(255, 255, 255);  // Set the fill color to white
  }
  ellipse(redRadioButtonX, redRadioButtonY, radioButtonSize / 2, radioButtonSize / 2);  // Draw the red radio button indicator
  ellipse(greenRadioButtonX, greenRadioButtonY, radioButtonSize / 2, radioButtonSize / 2);  // Draw the green radio button indicator
  ellipse(blueRadioButtonX, blueRadioButtonY, radioButtonSize / 2, radioButtonSize / 2);  // Draw the blue radio button indicator
  ellipse(yellowRadioButtonX, yellowRadioButtonY, radioButtonSize / 2, radioButtonSize / 2);  // Draw the yellow radio button indicator
  ellipse(whiteRadioButtonX, whiteRadioButtonY, radioButtonSize / 2, radioButtonSize / 2);  // Draw the white radio button indicator
}

void mousePressed() {
  // Check if the mouse is over the "ON" button
  if (mouseX > onButtonX && mouseX < onButtonX + buttonWidth && mouseY > onButtonY && mouseY < onButtonY + buttonHeight) {
    port.write("1");  // Send the "ON" command to the Arduino
    println("ON");  // Print "ON" to the serial monitor
  }

  // Check if the mouse is over the "OFF" button
  if (mouseX > offButtonX && mouseX < offButtonX + buttonWidth && mouseY > offButtonY && mouseY < offButtonY + buttonHeight) {
    port.write("0");  // Send the "OFF" command to the Arduino
    println("OFF");  // Print "OFF" to the serial monitor
  }
}


  
