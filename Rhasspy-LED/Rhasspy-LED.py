#!/usr/bin/env python
from apa102_pi.driver import apa102
from time import sleep
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
import os

rhasspyConfig = '/root/.config/rhasspy/profiles/de/profile.json'

counter = 0
LED = "on"
mute = "off"
siteId = ""
MQTThost = ""

with open(rhasspyConfig,'r', encoding='utf-8') as file:
    obj = json.loads(file.read())
    MQTTconfig = json.dumps(obj["mqtt"])
    MQTTconfig = MQTTconfig.replace("\"mqtt\": ","")
    MQTTconfig = json.loads(MQTTconfig)
    siteId = json.dumps(MQTTconfig["site_id"])
    MQTThost = json.dumps(MQTTconfig["host"])
    MQTThost = MQTThost.strip('"')
    if "port" in json.dumps(MQTTconfig):
      MQTTport = json.dumps(MQTTconfig["port"])
      MQTTport = MQTTport.strip('"')
      MQTTport = int(MQTTport)
    else:
      MQTTport = 1883

strip = apa102.APA102(num_led=4)
strip.clear_strip()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("hermes/dialogueManager/sessionEnded/#")
    client.subscribe("hermes/hotword/toggleOff/#")

def on_message(client, userdata, msg):
    if msg.topic == "hermes/hotword/toggleOff" and "dialogueSession" in str(msg.payload) and '"siteId": ' + siteId in str(msg.payload) and LED == "on":
      strip.set_pixel(1,0,255,0,7)
      strip.show()
    elif msg.topic == "hermes/dialogueManager/sessionEnded" and '"siteId": ' + siteId in str(msg.payload):
      strip.set_pixel(1,0,255,0,0)
      strip.show()
    elif str(msg.payload) == 'b\'{"siteId": ' + siteId + ', "reason": "ttsSay"}\'' and LED == "on":
      strip.set_pixel(1,0,0,255,7)
      strip.show()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTThost, MQTTport, 60)
client.loop_start()

BUTTON = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

while True:
    state = GPIO.input(BUTTON)
    if state:
      counter = 0
    else:
      counter = counter + 1
      if counter == 10:
        strip.set_pixel(1,255,0,0,50)
        strip.show()
        sleep(2)
        strip.set_pixel(1,0,0,0,0)
        sleep(.2)
        os.system("shutdown -h now")
      elif counter == 3 and mute == "off":
        mute = "on"
        LED = "off"
        os.system("amixer -q -c 'seeed2micvoicec' sset Capture 0")
      elif counter == 3 and mute == "on":
        mute = "off"
        LED = "on"
        os.system("amixer -q -c 'seeed2micvoicec' sset Capture 63")
      elif counter == 1 and LED == "on":
        LED = "off"
      elif counter == 1 and LED == "off":
        LED = "on"
      sleep(.8)
    sleep(.2)
