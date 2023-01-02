import apsync.*;
import processing.serial.*;

PFont f;
AP_Sync streamer;

public String doorState;

public int Red;
public int Green;
public int Blue;

void setup(){
  size(500,300);

  streamer = new AP_Sync(this,"COM3", 9600);

  background(0);
  f = createFont("Arial",36,true);
  textFont(f,36);
  fill(255);
}

void draw() {
  background(0);
  textAlign(CENTER);
  if(Red != -1 &&  Green != -1 && Blue != -1){
    background(Red,Green,Blue);
  }
  if(doorState != null){
    text(doorState,width/2,height/2);
  }
}
