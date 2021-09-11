# -*- coding: utf-8 -*-



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial 
import pymysql
import time
import urllib.request
import requests
import threading
import json

import random 

def thingspeak_post(val1,val2,val3,val4):
    #threading.Timer(15,thingspeak_post).start()
    #val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='EHH500EDYZ0Y9GNF'
    HEADER='&field1={}&field2={}&field3={}&field4={}'.format(val1,val2,val3,val4)
    NEW_URL=URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

device = 'COM3' #this will have to be changed to the serial port you are using
try:
    arduino = serial.Serial(device, 9600, timeout=5)
    print("Trying...",device )
 
except:
    arduino.close()  
    print ("Failed to connect on",device )   
                   

try:
      while True:
          data = arduino.readline() #the last bit gets rid of the new-line chars
          #print(data)
          data1=str(data)
          data1=data1.replace("b'","").replace("r","").replace("n","").replace("\\","").replace("'","")
          pieces = data1.split(",")
          if len(pieces)>1:
              print(pieces)
              thingspeak_post(pieces[0],pieces[1],pieces[2],pieces[3])


except:
    arduino.close()
    print("Failed to get data from Arduino!")

            
            

