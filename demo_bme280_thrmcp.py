#Implementation of BME280/BME680 and MCP9600/thermocouple interfacing with Raspberry Pi
#Sensing data are saved in a file named after the date
#Jin Zhu created 5/25/2023

import time
from datetime import datetime
import re
import sys
import board
from adafruit_bme280 import basic as BME280   #library for BME280
from adafruit_mcp9600 import MCP9600  #libary for MCP9600
from savedata_locally import savedata_locally as document

#I2C setup
i2cbus = board.I2C() #use default raspberry pi board SCL and SDA for I2C
#BME280 setup
mybme280=BME280.Adafruit_BME280_I2C(i2cbus,0x77)  #the default I2C address is 0x77 for adafruit BME280 board.
#use BME280.Adafruit_BME280_I2C(i2cbus, 0x76) instead if the I2C address is 0x76
#MCP9600 setup
thmcp = MCP9600(i2cbus,0x67, 'K')
#The default I2C address is 0x67 for adafruit MCP9600 board, range: 0x60-67
#Indicate the thermocouple used is K type. The default type is K and other
#options: 'J','T','N','S','E','B' or 'R'

#indicate the field meaning in the test
datatype = "Date, Time, Temperature(C), Pressure(hPa), Humidity(%), Thermocouple K(@0x67) Temperature(C)"
try: 
     print("Start reading data from BME280 and thermocouple K......\n")
     print(datatype)
     while True:
      timestamp = str(datetime.now()) #obtain current time
     
      #BME280 results
      temperature = mybme280.temperature #obtain the ambient temprature in Celsius degree
      pressure = mybme280.pressure  #obtain the pressure in hPa
      humidity = mybme280.humidity  #obtain the relative humidity in percentage

      #obtain thermocpule result
      typeK_tmp = thmcp.temperature 

      timestamp = re.sub(' ',', ', timestamp)
      #timestamp = timestamp.split('.')[0] #uncomment this line if omitting subseconds time information
      output = timestamp + ", {0:.2f}, {1:.2f}, {2:.2f},{2:.2f}".format(temperature, pressure, humidity, typeK_tmp)

      print(output)  #display results in the terminal
      document(output, datatype)  #save data into a local text file
      time.sleep(4.85) #data are collected roughly every 5 second

except KeyboardInterrupt:
      print("Interrupted by User")
      sys.exit(0)
