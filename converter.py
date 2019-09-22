# - TETRACONTROL CONVERTER -
# A tetracontrol extension software

version = "1.0.0"

import os
import time
from PIL import Image

print("-------------------------\n  tetraconverter v"+version+"\n-------------------------\n// © 2019 - PrismArray Software\n// (admin@prismarray.net)")

while True:
	cmd = input("\nAvailable commands: 'convert'\n>> ")

	if cmd == "convert":
		while True:
			filename = input("\nPlease enter the filename of your image.\n>> ")
			print("\n[i] Attempting to load '"+filename+"'...")
			try:
				img = Image.open(filename)
				pix = img.load()
				break
			except:
				print("[!] Invalid file.")
			
		print("[i] Image successfully loaded!")

		def eq(a):
			return 6-a

		with open("out.txt", "a") as outfile:
			outfile.write("{ //image\n")
			for i in range(0,7):
				for ii in range(0,7):
					if i == 0 or i == 2 or i == 4 or i == 6:
						outfile.write("{"+str(pix[ii,i][0])+", "+str(pix[ii,i][1])+", "+str(pix[ii,i][2])+"}")
						if ii == 6:
							if i == 6:
								outfile.write(" },")
							else:
								outfile.write(",\n")
						else:
							outfile.write(", ")
					else:
						outfile.write("{"+str(pix[6-ii,i][0])+", "+str(pix[6-ii,i][1])+", "+str(pix[6-ii,i][2])+"}")
						if ii == 6:
							outfile.write(",\n")
						else:
							outfile.write(", ")
		print("\n[i] Successfully converted your image.")

	else:
		print("[!] Invalid command.\n")