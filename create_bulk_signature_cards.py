#create a bunch of signature cards

#imports
from PIL import Image, ImageDraw, ImageFont
import cv2
try:
	import random
except:
	print("Random not installed. pip install random. Exiting now.")
	exit()
try:
	import csv
except:
	print("CSV not installed. Google the PIP command to install. Exiting now.")
	exit()
try:
	import os
except:
	print("os not installed. Google the PIP command to install. Exiting now.")
	exit()

try:
	import qrcode
except:
	print("qr code not installed. QR Codes will not be created. Exiting now.")
	exit()

#used for the loop to get user to enter a valid number.
numberSet = True #while testing, set this equal to true to avoid the loop. True will just use the below number whereas False will prompt the loop
number = 50


while numberSet == False:
	try:
		number = int(input("How many signature cards do you want to create?"))
		number = number - 1 #We will use range later, which I believe includes 0
		Numberset = True
		break
	except:
		print("Please enter an integer.")



#checks for the created folder
if not os.path.exists('scans'):
	os.makedirs('scans')

#loop to create signature cards
for number in range(number):
	sigcard = Image.open('template.jpg')

	#generates new name
	first_names_list = []
	with open("misc/first_names.txt") as first_name_file:
		first_names = csv.reader(first_name_file)

		for name in first_names:
			for name in name:
				if name != '':
					first_names_list.append(name)
	#print(first_names_list)

	last_names_list = []
	with open("misc/last_names.txt") as last_name_file:
		last_names = csv.reader(last_name_file)

		for name in last_names:
			for name in name:
				if name != '':
					last_names_list.append(name)
	#print(last_names_list)
	randomname = random.choice(first_names_list) + " " + random.choice(last_names_list)


	#writes name
	name = ImageDraw.Draw(sigcard)
	name.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 45) 
	name.text((405,387), randomname, font = name.font, fill=(0,0,0))

	#writes new account number
	accountnumber = str(random.randint(100000001, 999999999))
	account = ImageDraw.Draw(sigcard)
	account.font = ImageFont.truetype(r'C:\Windows\Fonts\Times New Roman\timesbd.ttf', 45) 
	account.text((495,423), accountnumber, font = account.font, fill=(0,0,0))
	#sigcard.save(f"created/{number}.jpg")

	#adds qr code
	if random.randrange(0,2) == 1:
		qrmessage = f"document name: signature card - account number: {str(accountnumber)} - name1: {randomname}"
		print(qrmessage + " " + str(number))
		qrcodeimg = qrcode.make(qrmessage, box_size=11)
		#qrcodeimg = qrcodeimg.resize((200,200))
		sigcard.paste(qrcodeimg, (1900,2400))
		#(2443, 3225)


	
	sigcard.save(f"scans/scan_number_{number+1}.jpg")

print("Done!")
exit()