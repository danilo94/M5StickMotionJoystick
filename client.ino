#include <M5StickC.h>
#include <math.h>
#include <WiFi.h>
#include <WiFiUdp.h>
#define PITCH_LIMIT 28
#define ROLL_LIMIT 28
const char * ssid = "";
const char * pwd = "";
const char * udpAddress = "192.168.100.6";
const int udpPort = 44444;
#include "AsyncUDP.h"
float accX = 0;
float accY = 0;
float accZ = 0;

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  pinMode(M5_BUTTON_HOME, INPUT);
  M5.begin();
  M5.Lcd.fillScreen(TFT_BLACK);
  M5.Lcd.setTextSize(1);
  M5.MPU6886.Init();
  WiFi.begin(ssid,pwd);
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(100);
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  //This initializes udp and transfer buffer
}
bool estadoAnterior = false;
void loop() {

    if (digitalRead(M5_BUTTON_HOME)==LOW){
      estadoAnterior = !estadoAnterior;
      Serial.println(estadoAnterior);
      delay(10);
    }
  
    M5.MPU6886.getAccelData(&accX,&accY,&accZ);
    M5.Lcd.setCursor(0, 20);
    float accelerationX = (float)(((float)accX) * 3.9);
    float accelerationY = (float)(((float)accY) * 3.9);
    float accelerationZ = (float)(((float)accZ) * 3.9);

    byte pressed = keypressed(accelerationX,accelerationY,accelerationZ);
    if(estadoAnterior){
          udp.beginPacket(udpAddress,udpPort);
          udp.print(pressed);
          udp.endPacket();
    }
    delay(200);
}

byte keypressed(float accelerationX,float accelerationY,float accelerationZ){
    float pitch = 180 * atan (accelerationX/sqrt(accelerationY*accelerationY + accelerationZ*accelerationZ))/M_PI;
    float roll = 180 * atan (accelerationY/sqrt(accelerationX*accelerationX + accelerationZ*accelerationZ))/M_PI;
    M5.Lcd.print(roll);
    M5.Lcd.setCursor(0,40);
    M5.Lcd.print(pitch);
    byte pressed = 0;
    if (pitch > PITCH_LIMIT){
      pressed = pressed | 1;
    }
    if (pitch <PITCH_LIMIT*-1){
      pressed = pressed | 2;
    }

    if (roll > ROLL_LIMIT){
      pressed = pressed | 4;
    }
    if (roll <ROLL_LIMIT*-1){
      pressed = pressed | 8;
    }
    return pressed;
}
