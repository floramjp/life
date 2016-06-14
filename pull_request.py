
from lifxlan import *
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
# helios
helios = '**confidential**'
response = requests.get(helios, auth=('floramjp', '**confidential**'))
response_json = response.json()
response_dict = json.dumps(response_json)
load_dict = json.loads(response_dict)

# Update initial time
print "Initialization! Current time is: " + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
init_time = datetime.datetime.now() - datetime.timedelta(minutes=20)

while True :
	for x in load_dict:
		tics_time = datetime.datetime.strptime(x["updated_at"], "%Y-%m-%dT%H:%M:%SZ")
		if tics_time > init_time:
			# Note: Github API brings thins in +4 hours time, so will neutralize
			tics_str = (tics_time - datetime.timedelta(hours=4)).strftime("%Y-%m-%dT%H:%M:%SZ")
			print "************************************************************"
			print "PR number: " + str(x["number"])
			print "PR user login: " + x["user"]["login"]
			print "PR title: " + x["title"]
			print "PR updated_at timestamp: " + tics_str
			x["updated_at"]
			print "************************************************************"
			init_time = tics_time
		
			# alert bulb
			bulb.set_color(BLUE)
			sleep(1)
			bulb.set_color(original_color)
	
	# sleep for 5 minutes
	sleep(300)
	response = requests.get(helios, auth=('floramjp', '**confidential**'))
	response_json = response.json()
	response_dict = json.dumps(response_json)
	load_dict = json.loads(response_dict)
	print "Current time is: " + datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
