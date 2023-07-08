/*
  NodeMCU Demo Code

  Read temperature, pressure, and humidity data from an BME280 via I2C 
  and display the results in the Serial Monitor. 

  Created June 8 2023 by Jin Zhu

  This example code is under MIT license and available at 
  https://github.com/JZ2211/IIoT_module5/blob/main/demo_NodeMCU.ino

*/

//libraries for BME280
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme280; //I2C

void setup() {
  Serial.begin(115200);         // Start the Serial communication to send messages to the computer
  while (!Serial) {} //wait till serial is connected  
  delay(10);  //delay 10 milliseoncds to make sure serial port is connected
  Serial.println("start...."); // for debugging

  char status=bme280.begin();
  while (!status){
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x"); 
        Serial.println(bme280.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("        ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1) delay(10);  //stop the code here if BME280/680 is not found
  }

}

//the loop() function will repeat running forever
void loop() {
  unsigned int temperature, pressure, humidity;
  temperature = bme280.readTemperature(); 
  pressure = bme280.readPressure();
  humidity = bme280.readHumidity();

  Serial.print("Time Stamp(s)");
  Serial.println(millis()/1000);
  Serial.print(" Temperature (degC): ");
  Serial.print(temperature);
  Serial.print(", Pressure (Pa): ");
  Serial.print(pressure);
  Serial.print(", Humidity (%): ");
  Serial.println(humidity);

  delay(2000); //delay 2000 milliseconds so that update data every 2 seconds
}
