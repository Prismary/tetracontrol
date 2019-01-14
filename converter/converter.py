# - TETRACONTROL CONVERTER -
# A tetracontrol extension software

version = "0.0.1"

import time
from PIL import Image

print("-------------------------\n  tetraconverter v"+version+"\n-------------------------\n// PrismArray Software (admin@prismarray.net)\n")

while True:
	cmd = input("\nAvailable commands: 'convert'\n>>")

	if cmd == "convert":
		config = open("display.json", "x")
		config.write("{\n")
		while True:
			imgcount = input("\nPlease enter the count of images you want.\n>>")
			try:
				imgint = int(imgcount)
				break
			except:
				print("[!] Invalid image count.")
		while True:
			miscinfo = input("\nPlease provide mode and delay seperated as seen below.\nmode~delay\n>>")
			try:
				mode = miscinfo.split("~")[0]
				delay = miscinfo.split("~")[1]
				test = int(mode)+int(delay)
				break
			except:
				print("[!] Invalid input.")
		config.write("\"")
		imcounter = 0
		while True:
			imcounter = imgcounter+1
			if imgint == 0:
				break
			filename = input("\nPlease enter the filename of image "+str(imcounter)+".\n>>")
			print("[i] Attempting to load '"+filename+"'...")
			try:
				img = Image.open(filename)
				pix = img.load()
			except:
				print("[!] Invalid file.")
			if img.size != "(7, 7)":
				print("[!] Invalid image size. Must be 7x7!")
			else:
				imgint = imgint-1
				continue
		print("[i] Image successfully loaded!")

	else:
		print("[!] Invalid command.\n")