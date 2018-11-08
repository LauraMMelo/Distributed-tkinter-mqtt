#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 15:59:32 2018

@author: computervision
"""
import paho.mqtt.client as paho
import time
from tkinter import *

lampada_message = ''   #HERE!
arcond_message = ''
temp_sensor_message = ''
gelad_message = ''
porta_message = ''



def on_message(client, userdata, msg):
    global arcond_message, temp_sensor_message, gelad_message, porta_message
#    if msg.topic == 'house/lampada':
#        lampada_message  = str(msg.payload)   #HERE!
#        print(msg.topic+" "+str(msg.payload))
    
    if msg.topic == 'house/arcond':
        arcond_message  = str(msg.payload)   #HERE!
        print(msg.topic+" "+str(msg.payload))
    
    if msg.topic == 'house/temp_sensor':
        temp_sensor_message = str(msg.payload)   #HERE!
        print(msg.topic+" "+str(msg.payload))
    
    if msg.topic == 'house/gelad':
        gelad_message = str(msg.payload)   #HERE!
        print(msg.topic+" "+str(msg.payload))
    
    if msg.topic == 'house/porta':
        porta_message  = str(msg.payload)   #HERE!
        print(msg.topic+" "+str(msg.payload))

class Application:
    def __init__(self, master= None):
        self.lampada_message = ''
        self.arcond_message = ''
        self.temp_sensor_message = ''
        self.gelad_message = ''
        self.porta_message = ''
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.titulo = Label(self.container1, text = "Controlador MQTT")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        
        self.lampada = Label(self.container2, text = "Lampada")
        self.lampada.pack(side=LEFT)
        
        self.lamp_estado = Button(self.container2, text= 'OFF')
        self.lamp_estado["width"] = 10
        self.lamp_estado["font"] = self.fonte
        self.lamp_estado.bind("<Button-1>", self.mudarTexto)
        self.lamp_estado.pack(side=LEFT)

        self.arcond = Label(self.container3, text = "Ar Condicionado")
        self.arcond.pack(side=LEFT)
        
        self.arcond_estado = Label(self.container3, text="On")
        self.arcond_estado["width"] = 10
        self.arcond_estado["font"] = self.fonte
        self.arcond_estado.pack(side=LEFT)  
        
        self.temp_sensor = Label(self.container4, text = "Sensor de Temperatura")
        self.temp_sensor.pack(side=LEFT)
        
        self.temp_sensor_estado = Label(self.container4, text="On")
        self.temp_sensor_estado["width"] = 10
        self.temp_sensor_estado["font"] = self.fonte
        self.temp_sensor_estado.pack(side=LEFT)  

        self.gelad = Label(self.container5, text = "Geladeira")
        self.gelad.pack(side=LEFT)
        
        self.gelad_estado = Label(self.container5, text="On")
        self.gelad_estado["width"] = 10
        self.gelad_estado["font"] = self.fonte
        self.gelad_estado.pack(side=LEFT) 
        
        self.porta = Label(self.container6, text = "porta")
        self.porta.pack(side=LEFT)
        
        self.porta_estado = Label(self.container6, text="On")
        self.porta_estado["width"] = 10
        self.porta_estado["font"] = self.fonte
        self.porta_estado.pack(side=LEFT) 
        
        
    def mudarTexto(self, event):
        
        if self.lamp_estado["text"] == "OFF":
            self.lamp_estado["text"] = "ON"
#            update_value("ON")
        else:
            self.lamp_estado["text"] = "OFF"
#            update_value("OFF")


#    def update_variables(self):
#        self.lamp_estado = lampada_message
#        self.arcond_message = arcond_message
#        self.comp_message = comp_message
#        self.gelad_message = gelad_message
#        self.porta_message = porta_message
        
        
def update_value(state):
    global lampada_message
    lampada_message = state
#    print(lampada_message)
        
broker = "test.mosquitto.org"
client = paho.Client("Application1")

client.on_message = on_message

print("connecting to broker ", broker)

client.connect(broker)
client.loop_start()
        
root = Tk()
app = Application(master=root)

LOOP_ACTIVE =True
while LOOP_ACTIVE:
    root.update()
    client.subscribe([('house/arcond',2),('house/temp_sensor',2),('house/gelad',2),('house/porta',2)])
    app.temp_sensor_estado.configure(text=temp_sensor_message)
    app.arcond_estado.configure(text=arcond_message)
    app.gelad_estado.configure(text=gelad_message)
    app.porta_estado.configure(text=porta_message)
#    update_value(app.lamp_estado["text"])
    client.publish("house/lampada", str(app.lamp_estado["text"]))
    client.loop(.1)
    time.sleep(.5)
    print(app.lamp_estado["text"])
