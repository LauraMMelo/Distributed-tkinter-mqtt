#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:08:23 2018

@author: computervision
"""

import paho.mqtt.client as paho
import time

broker = "test.mosquitto.org"

##define callback

#def on_message(client, userdata, message):
#    time.sleep(1)
#    print("received message = ", str(message.payload.decode("utf-8")))

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")

#####bind function to callback
#client.on_message = on_message

print("connecting to broker ", broker)

client.connect(broker)
client.loop_start() #start loop to process received
#print("subscribing")
#client.subscribe("house/bulb1") #subscribe
#time.sleep(2)
#print("publishing")
try:
    while True:
        client.publish("house/temp_sensor/temperature", "23")#publish
        time.sleep(4)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect
    client.loop_stop()
