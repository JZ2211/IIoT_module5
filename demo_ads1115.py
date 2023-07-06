#Demo: implementation of reading analog input from a moisture sensor
#    via a 16-bit ADC with I2C interface ADS1115  
#Jin Zhu  Created 6/03/2023

import time
from datetime import datetime
import re
import sys
import board
from savedata_locally import savedata_locally as document
from adafruit_ads1x15.ads1115 import ADS1115
#for ADS1015: use the next line instead
#from adafruit_ads1x15.ads1015 import ADS1015
from adafruit_ads1x15.analog_in import AnalogIn

#use default raspberry pi board SCL and SDA for I2C
i2cbus = board.I2C()

# Create an ADS1115 ADC (16-bit) instance.
adc = ADS1115(i2cbus)

# Or create an ADS1015 ADC (12-bit) instance.
#adc = ADS1015()

# Note you can change the I2C address from its default (0x48) by passing in the parameter, for example:
#adc = ADS1115(i2cbus, address=0x49, gain=1)
# default gain of 1 for reading voltages from 0 to 4.096V for ADS1x15.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.


datatype ="Date, Time, voltage (V) "

#obtain single-ended analog data input from channel A0
chan = AnalogIn(adc, 0)

#singled-ended inputs: 0, 1, 2, 3
#differential input channels: (0,1), (0,3), (1,3), (2,3)
#an example for obtaining a differential input between pin A0 and A1:
#chan = AnalogIn(adc, 0, 1)

try: 
     print("start reading analog voltage input ....\n")
     print(datatype)
     while True:
      timestamp = str(datetime.now()) #obtain current time    
      timestamp = re.sub(' ',', ', timestamp)
      output = timestamp + ", {0:.5f}".format(chan.voltage)

      print(output)  #display results in the terminal
      document(output, datatype)  #save data into a local text file
      time.sleep(4.85) #data are collected roughly every 5 second
          

except KeyboardInterrupt:
     print("Interrupted by User")
     sys.exit(0)
