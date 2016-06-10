from lifxlan import *
from flask import Flask, jsonify
from time import sleep
import sys
import requests

lifx = LifxLAN()

# list of lights
lights = lifx.get_lights()
bulb = lights[0]

original_power = bulb.get_power()
original_color = bulb.get_color()
bulb.set_power("on")

all_power = lifx.get_power_all_lights()
all_color = lifx.get_color_all_lights()

light = bulb
interval = 1.5
num_cycles = 1

rainbow = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]

original_color = light.get_color()
rapid = True if interval < 2 else False

for i in range(num_cycles):
	for color in rainbow:
		bulb.set_color(color, rapid)
		sleep(interval)

light.set_color(original_color)
