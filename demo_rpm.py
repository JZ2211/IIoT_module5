#Demo: reading falling edge triggered pulses from pin GPIO_26 
#    Determine the RPM based on the elasped time between pulses
#Jin Zhu  Created 06/05/2023

import RPi.GPIO as GPIO
import time
from datetime import datetime
import sys

#connect to pin GPIO_26
channel = 26

#initialize the GPIO pin
def init_GPIO(channel):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.remove_event_detect(channel)

#use threaded callback: the function is called immediately in response to an edge triggered event
def my_callback(channel):
    global pulseCount, start_timer, elapse
    pulseCount +=1
    elapse = time.time() - start_timer
    start_timer = time.time()

#configure the interrupt is falling edge triggered. Use GPIO.RISING for rising edge triggered events
def init_interrupt(channel):
    GPIO.add_event_detect(channel, GPIO.FALLING, callback = my_callback, bouncetime = 20)


rpmlog = open('log_rpm.csv', 'a', buffering = 1)
rpmlog.write('RPM \n')

try: 
  pulseCount = 0
  elapse = 0
  init_GPIO(channel)
  init_interrupt(channel)
  start_timer = time.time()
  previousCount = 0
  print("starting... \n RPM:")
  while (True):
    time.sleep(1)
    if (elapse != 0) and (previousCount!= pulseCount):
         rpm = 1/elapse *60
         output = "%d, %d" %(rpm, pulseCount)
         previousCount = pulseCount
         print(output)
         rpmlog.write("%d"%(rpm)+"\n")   
     
except KeyboardInterrupt:
  print("interrupted by the User")
  rpmlog.close()
  sys.exit(0)



