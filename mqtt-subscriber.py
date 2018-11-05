#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:40:12 2018

@author: computervision
"""

import paho.mqtt.client as paho
import time

broker = "test.mosquitto.org"

##define callback

def on_message(client, userdata, message):
    time.sleep(.5)
    print("received message = ", str(message.payload.decode("utf-8")))

client= paho.Client("client-002") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

#####bind function to callback
client.on_message = on_message

print("connecting to broker ", broker)

client.connect(broker)
client.loop_start() #start loop to process received
print("subscribing")
client.subscribe("house/lampada") #subscribe
#time.sleep(2)

try:
    while True:
        time.sleep(.1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect
    client.loop_stop()
