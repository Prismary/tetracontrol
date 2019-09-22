# - TETRACONTROL -
# A Tetrapix controller software

version = "1.1.0"

import requests
import time
import serial
import json
import datetime

print("   __       __                              __             __\n  / /____  / /__________ __________  ____  / /__________  / /\n / __/ _ \/ __/ ___/ __ `/ ___/ __ \/ __ \/ __/ ___/ __ \/ /\n/ /_/  __/ /_/ /  / /_/ / /__/ /_/ / / / / /_/ /  / /_/ / /\n\__/\___/\__/_/   \__,_/\___/\____/_/ /_/\__/_/   \____/_/")

print("[tetracontrol v"+version+"]\n// PrismArray Software (admin@prismarray.net)]\n\n")
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
print("Config successfully loaded!")
config.close()

print("\nEstablishing connection to controller device...")
time.sleep(2)
ser = serial.Serial(serid, 9600)
print("Connection established.")

print("\n[i] Done! Now setting up the display loop.\n")

def ctime():
	return str(datetime.datetime.now())[11:19]

def sendscreen(img):
	for i in range(0,49):
		for j in range(0,3):
			ser.write(int(data["screendata"][img][i][j]))

while True:
	if readmode == "cloud":
		try:
			jsondata = requests.get(url).text
			data = json.loads(jsondata)
			print("[i] Server data loaded.")
		except:
			print("[!] Failed to get server data.")
	else:
		try:
			with open(filename,"r") as jsondata:
				data = json.loads(jsondata)
			print("[i] Local data loaded.")
		except:
			print("[!] Failed to get local data.")

	mode = int(data["mode"])
	delay = int(data["delay"])
	imgcount = int(data["imgcount"])
	print("[i] Starting up in mode "+str(mode)+".")
	if mode == 0:
		print("["+ctime()+"] Updating display...")
		sendscreen(0)
		print("["+ctime()+"] Done!")
		time.sleep(rfdelay)
		print("["+ctime()+"] Refreshing display data...")
	elif mode == 1:
		for i in range(0,10):
			j = 0
			while j < imgcount:
				sendscreen(j)
				time.sleep(delay)
				j = j+1
		print("[i] Refreshing display data.")
	elif mode == 99:
		print("[i] Now running in TEST mode.\n[!] This mode is for DEVELOPMENT ONLY!")
		sendscreen(0)
		time.sleep(5)
	else:
		print("[!] Invalid mode. Refreshing in "+str(rfdelay)+" seconds.")
		time.sleep(rfdelay)
