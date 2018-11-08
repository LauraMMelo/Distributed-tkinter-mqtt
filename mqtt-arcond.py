#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:08:23 2018

@author: computervision
"""

import paho.mqtt.client as paho
import time

broker = "test.mosquitto.org"


client= paho.Client("client-002") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")



print("connecting to broker ", broker)

client.connect(broker)
client.loop_start() #start loop to process received
try:
    while True:
        client.publish("house/arcond", str("On"))#publish
        time.sleep(2)
        

except KeyboardInterrupt:
    print("exiting")
    client.disconnect
    client.loop_stop()
