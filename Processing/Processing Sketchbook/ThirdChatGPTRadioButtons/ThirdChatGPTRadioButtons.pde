import processing.serial.*;
import controlP5.*;
import apsync.*;

ControlP5 cp5;
AP_Sync ap;

void setup() {
  size(200, 200);

  // Set up the ControlP5 library
  cp5 = new ControlP5(this);

  // Set up the radio buttons
  cp5.addRadioButton("colorRadio")
    .setPosition(50, 50)
    .setSize(20, 20)
    .setItemsPerRow(1)
    .setSpacingColumn(50)
    .addItem("redRadio", 1)
    .addItem("greenRadio", 2)
    .addItem("blueRadio", 3)
    .addItem("yellowRadio", 4)
    .addItem("whiteRadio", 5)
    .activate(0);

  // Set up the on/off buttons
  cp5.addButton("onButton")
    .setPosition(50, 100)
    .setSize(50, 20)
    .setLabel("On")
    .onPress(new CallbackListener() {
      public void controlEvent(CallbackEvent event) {
        onButtonPressed();
      }
    });
  cp5.addButton("offButton")
    .setPosition(100, 100)
    .setSize(50, 20)
    .setLabel("Off")
    .onPress(new CallbackListener() {
      public void controlEvent(CallbackEvent event) {
        offButtonPressed();
      }
    });

  // Set up the APSync library
  ap = new AP_Sync(this, "COM3", 9600);
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
    ap.send((int)selectedColorIndex);
  }
}


// Handle the on button press event
void onButtonPressed() {
  println("On button pressed");
  ap.send(1);
}

// Handle the off button press event
void offButtonPressed() {
  println("Off button pressed");
  ap.send(0);
}
