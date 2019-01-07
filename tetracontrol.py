# - TETRACONTROL -
# A Tetrapix controller software made by Prismary.

version = "0.0.1"

import requests
import time
import serial
import json

# Serial Commands
# 'refresh' - Refreshes the image
# 'data []' - Sends an image array

def sendscreen(data):
	ser.write(b'data '+data)
	
print("-----------------------\n  tetracontrol v"+version+"\n-----------------------\n")
print("> Starting up...\n")
print("Loading config...")
errors = 0
try:
	config = open("config.txt","r")
except:
	print ("[!] Unable to load 'config.txt'.\nPlease restore the file and restart tetracontrol.")
	time.sleep(5)
	exit()
for line in config:
	# Serial-ID
	if "serial-id" == line.split(": ")[0]:
		if "COM" in line.split(": ")[1].replace("\n", ""):
			serid = line.split(": ")[1].replace("\n", "")
			print ("Serial-ID:	"+serid)
		else:
			print ("[!] Failed to load 'Serial-ID'")
			errors = errors+1
	# Read-Mode
	if "read-mode" == line.split(": ")[0]:
		if "cloud" or "local" == line.split(": ")[1].replace("\n", ""):
			readmode = line.split(": ")[1].replace("\n", "")
			print ("Read-Mode:	"+readmode)
		else:
			print ("[!] Failed to load 'Read-Mode'")
			errors = errors+1
	# Filename
	if "filename" == line.split(": ")[0]:
		if ".json" in line.split(": ")[1].replace("\n", ""):
			filename = line.split(": ")[1].replace("\n", "")
			print ("Filename:	"+filename)
		else:
			print ("[!] Failed to load 'Filename'")
			errors = errors+1
	# URL
	if "url" == line.split(": ")[0]:
		if "://" in line.split(": ")[1].replace("\n", ""):
			url = line.split(": ")[1].replace("\n", "")
			print ("URL:		"+url)
		else:
			print ("[!] Failed to load 'URL'")
			errors = errors+1
	# Refresh-Delay
	if "rf-delay" == line.split(": ")[0]:
		try:
			rfdelay = int(line.split(": ")[1].replace("\n", ""))
			print ("RF-Delay:	"+str(rfdelay))
		except:
			print ("[!] Failed to load 'RF-Delay'")
			errors = errors+1

	if "info" == line.replace("\n", ""):
		print("\n[!] Dieses Projekt wurde für den Informatik-Kurs 10ab des IKG erstellt.\n")
		
if errors > 0:	
	if errors == 1:
		print ("\n[!] Config loaded, "+str(errors)+" issue found.")
	else:
		print ("\n[!] Config loaded, "+str(errors)+" issues found.")
	print ("Please check 'config.txt' and restart tetracontrol.")
	time.sleep(5)
	exit()
print("Config successfully loaded!\n")

print("Establishing connection to controller device...")
time.sleep(2)
serid = serial.Serial(sernumber, 9600)
print("Connection established.")

print("\n[i] Done! Now running the display loop.\n")

while True:
	if readmode == "cloud":
		try:
			jsondata = requests.get(url).text
			data = json.loads(jsondata)
		except:
			print("[!] Failed to get server data.")
	else:
		try:
			jsondata = open(filename+".json","r")
			data = json.loads(jsondata)
		except:
			print("[!] Failed to get local data.")

	mode = int(data["mode"])
	delay = int(data["delay"])
	imgcount = int(data["imgcount"])
	if mode == 0:
		print("[i] Now running in mode "+str(mode)+".")
		sendscreen(data[screendata][0])
		time.sleep(rfdelay)
		print("[i] Refreshing server data.")
	elif mode == 1:
		print("[i] Now running in mode "+str(mode)+".")
		for i in range(0,10):
			i2 = 0
			while i2 < imgcount:
				sendscreen(data[screendata][i2])
				time.sleep(delay)
				i2 = i2+1
		print("[i] Refreshing server data.")
	else:
		print("[!] Invalid mode. Refreshing in "+str(rfdelay)+" seconds.")
		time.sleep(rfdelay)

# hooray.