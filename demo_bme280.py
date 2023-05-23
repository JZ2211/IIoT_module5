#implementation of BME280 or BME680 interfacing with Raspberry Pi
#data are saved in a file named after the date
#Jin Zhu created 5/18/2023

import time
from datetime import datetime
import re
import sys
import board
from adafruit_bme280 import basic as BME280
from savedata_locally import savedata_locally as document

#BME280 setup
i2cbus = board.I2C() #use default raspberry pi board SCL and SDA for I2C
mybme280=BME280.Adafruit_BME280_I2C(i2cbus,0x77)  #the default I2C address is 0x77 for adafruit BME280 board.
#use BME280(i2cbus, 0x76) instead if the I2C address is 0x76 

datatype = "Date, Time, Temperature(C), Pressure(hPa), Humidity(%)"
try: 
     print("Start reading data from BME280......\n")
     print(datatype)
     while True:
      timestamp = str(datetime.now()) #obtain current time
     
      #BME280 results
      temperature = mybme280.temperature #obtain the ambient temprature in Celsius degree
      pressure = mybme280.pressure  #obtain the pressure in hPa
      humidity = mybme280.humidity  #obtain the relative humidity in percentage        

      timestamp = re.sub(' ',', ', timestamp)
      #timestamp = timestamp.split('.')[0] #omit subseconds time information
      output = timestamp + ", {0:.2f}, {1:.2f}, {2:.2f}".format(temperature, pressure, humidity)
      #timestamp=timestamp.split('.')[0]

      print(output)  #display results in the terminal
      document(output, datatype)  #save data into a local text file
      time.sleep(4.85) #data are collected roughly every 5 second

except KeyboardInterrupt:
      print("\nUser interrupt")
      sys.exit(0)
