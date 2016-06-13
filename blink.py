from lifxlan import *
import time
import sys

import requests
import datetime
import json

lifx = LifxLAN()

# list of lights
lights = lifx.get_lights()
bulb = lights[0]

original_power = bulb.get_power()
original_color = bulb.get_color()
bulb.set_power("on")

all_power = lifx.get_power_all_lights()
all_color = lifx.get_color_all_lights()

# ---------------------------------------------------------------------------- #

# url for helios
helios = "confidential"

# update 1 minute before now (~ approximately status quo)
update = datetime.datetime.now() - datetime.timedelta(minutes=120)
tics = update.strftime("%Y-%m-%dT%H:%M:%SZ")
url = helios + "?since=" + tics

# response from github
response = requests.get(url, auth=('floramjp', "confidential"))
response_dict = response.json()
response_dict = json.dumps(response_dict)
print response_dict
recent_push = response_dict[0]["commit"]["committer"]["date"]
print "Most recent push " + recent_push

while True :
	
	# delay for 3 minutes
	time.sleep(180)

	# update 3 minute before now
	update = datetime.datetime.now() - datetime.timedelta(minutes=3)
	tics = update.strftime("%Y-%m-%dT%H:%M:%SZ")
	print "3 minutes passed, now time is: " + tics

	# response from github
	response = requests.get(url, auth=('floramjp', "confidential"))
	response_dict = response.json()
	response_dict = json.dumps(response_dict)
	temp = response_dict[0]["commit"]["committer"]["date"]

	if (temp != recent_push) :
		recent_push = temp
		print "updated most recent push "

		light = bulb
		interval = 0.5
		num_cycles = 1

		rainbow = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]

		original_color = light.get_color()
		rapid = True if interval < 2 else False

		for i in range(num_cycles):
			for color in rainbow:
				bulb.set_color(color, rapid)
				sleep(interval)

		light.set_color(original_color)