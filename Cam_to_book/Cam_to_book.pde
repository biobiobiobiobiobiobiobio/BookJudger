import processing.video.*;
import java.awt.*;
import processing.core.PImage;
import java.io.*;

Capture video;
int seed;
//float realWidth = 1280, realHeight = 720;
String rating = "", hdrating = "";
void setup() {
  //size(1280, 720);
  fullScreen();
  video = new Capture(this, 1280, 720);
  seed = (int)random(999999);

  video.start();
}

void draw() {
  randomSeed(seed);
  scale(1.5);
  image(video, 0, 0 );
  scale(.666666);
  fill(0);
  rect(0,0,width/2 - height/3,height);
  rect(width/2 + height/3,0,width,height);
  fill(255);
  textSize(128);
  text(rating, 5, 100);
  text(hdrating, width-500, 100);
  fill(200);
  textSize(100);
  text("SD", 5, 200);
  text("HD", width-500, 200);
}

void keyPressed(){
  if(key == 'r'){
    PImage partialSave = get(width/2 - height/3,0,width/2 + height/3,height);
    partialSave.save("../shared/" + seed + ".jpg");
    try {
      Runtime.getRuntime().exec("python D:\\Code\\Hackathons\\BookJudger\\NeuralNet\\predict_from_existing_net.py " + "D:\\Code\\Hackathons\\BookJudger\\shared\\" + seed +".jpg");
      Runtime.getRuntime().exec("python D:\\Code\\Hackathons\\BookJudger\\NeuralNet\\predict_from_existing_net2.py " + "D:\\Code\\Hackathons\\BookJudger\\shared\\" + seed +".jpg");
      delay(50);
      String[] lines = loadStrings("output.txt");
      rating = lines[0].substring(0,4);
      lines = loadStrings("hdoutput.txt");
      hdrating = lines[0].substring(0,5);
      System.out.println(lines[0]);
    } catch(Exception e) {
    }
  }
  
}

void captureEvent(Capture c) {
  c.read();
}
