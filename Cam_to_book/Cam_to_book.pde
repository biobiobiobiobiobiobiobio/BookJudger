import processing.video.*;
import java.awt.*;
import processing.core.PImage;

Capture video;
int seed;
void setup() {
  size(640, 480);
  video = new Capture(this, 640/2, 480/2);
  seed = (int)random(999999);

  video.start();
}

void draw() {
  randomSeed(seed);
  scale(2);

  image(video, 0, 0 );

  stroke(255);
  fill(0);
  rect(0,0,80,240);
  rect(240,0,320,240);
  noFill();
  rect(80,0,160,240);
  for(int i = 0; i < 17; i ++){
    line(0,random(0,240),80,random(0,240));
    line(240,random(0,240),320,random(0,240));
  }
}

void keyPressed(){
  if(key == 'r'){
  PImage partialSave = get(80,0,160,240);
  partialSave.save("../" + seed + ".jpg");
  }
  try {
    Runtime.getRuntime().exec("python ../NerualNet/predict_from_existing_net.py " + "../shared/" + seed +".jpg");
    delay(3000);
    String[] lines = loadStrings("output.txt");
    text(lines[0], 0, 0);
  } catch(IOException e) {
  }
}

void captureEvent(Capture c) {
  c.read();
}
