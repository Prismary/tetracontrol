#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel strip = Adafruit_NeoPixel(49, 0, NEO_RGB + NEO_KHZ800);

byte r[49];
byte g[49];
byte b[49];

void setup() {
  
  strip.begin();
  strip.show();

  Serial.begin(9600);
}

void loop() {

  while(Serial.available() <= 0) {}


  if(


  String input = readSerialLine();

  if(!input.StartsWith("data [[")) {
    Serial.println("Invalid input! Line for display input must start with 'data [['!");
    continue;
  }

  input = input.substring(7, input.Length - 7 - 2);

//  String[] pixelValues = input.Split(new String[] {"], ["});

  for(int i = 0; i < 49; i++) {

    String str = pixelValues[i];
//    String[] temp = str.Split(new String[] {", "});

    byte r = (byte) Int32.Parse(temp[0]);
    byte g = (byte) Int32.Parse(temp[1]);
    byte b = (byte) Int32.Parse(temp[2]);

    disp[i] = new Pixel(r, g, b);
  }
  
  refreshScreen();
}


void refreshScreen() {

  for(int i = 0; i < 49; i++) {

    strip.setPixelColor(i, disp[i].r, disp[i].g, disp[i].b);
  }
  
  strip.show();
}




String readSerialLine() {

  String str = "";
  byte next;
  
  if(Serial.available() > 0) {
    next = Serial.read();

    if(next == '>') {
      next = Serial.read();
      
    }
  }

  return str;
}




