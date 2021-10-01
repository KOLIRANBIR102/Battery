# python script showing battery details
import psutil

# import the pyttsx3 engine which wil convert the text to speech
import pyttsx3
engine = pyttsx3.init()

# import the time module
import time

# get the information of the battery
battery = psutil.sensors_battery()

#print the current percentage of the battery
print("The battery is remaining " + str(battery.percent))

#loop to check whether the battery percentage is divisible by 10
while True:
	battery = psutil.sensors_battery()
	Message = " The Battery is remaining only " + str(battery.percent) + " percent"
	if battery.percent % 10 == 0:
		#convert the text to speech
		engine.say(Message)
		engine.runAndWait()
		#function to sleep the program for 20 seconds
		time.sleep(20)
	else:
		pass
