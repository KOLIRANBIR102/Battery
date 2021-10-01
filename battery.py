# python script showing battery details
import psutil

import pyttsx3
engine = pyttsx3.init()
import time

battery = psutil.sensors_battery()
print(str(battery.percent))

while True:
	battery = psutil.sensors_battery()
	Message = " Battery is remaining " + str(battery.percent) + " percent"
	if battery.percent % 10 == 0:
		engine.say(Message)
		engine.runAndWait()
		time.sleep(20)
	else:
		pass
