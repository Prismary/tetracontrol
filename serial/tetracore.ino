#include <Adafruit_NeoPixel.h>

Adafruit_NeoPixel strip = Adafruit_NeoPixel(49, 0, NEO_RGB + NEO_KHZ800);

byte r[49];
byte g[49];
byte b[49];

void setup() {
  Serial.begin(9600);
}

void loop() {

  while(Serial.available() <= 0) {
    //wait
  }

  delay(1000);
  
  for(int i = 0; i < 49; i++) {
    r[i] = Serial.read();
    g[i] = Serial.read();
    b[i] = Serial.read();
  }

  refreshScreen();
}

void refreshScreen() {

  for(int i = 0; i < 49; i++) {

    strip.setPixelColor(i, r[i], g[i], b[i]);
  }
  
  strip.show();
}

