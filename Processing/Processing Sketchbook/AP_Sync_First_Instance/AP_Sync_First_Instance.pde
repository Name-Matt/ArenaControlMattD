import apsync.*; // Include the library
import processing.serial.*; //Include Processing Serial

APSync streamer; // Create a variable named streamer of type APsync

void setup(){
     streamer = new APSync(this, "COM14", 9600); // Stump out an instance of APsync
}

void draw(){

}
