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
bypass = True

if bypass == False:
	while numberSet == False:
		try:
			number = int(input("How many signature cards do you want to create?"))
			number = number - 1 #We will use range later, which I believe includes 0
			Numberset = True
			break
		except:
			print("Please enter an integer.")

	while True and bypass == False:
		try:
			tiltSet = input("Do you want the scans to have a slight skew? Type yes or no.")
			break
		except:
			print("Please answer with either yes or no.")
else:
	number = 5
	tiltSet = True #do you want to tilt the scans? Only if bypass is set to true.

#checks for the created folder
if not os.path.exists('scans'):
	os.makedirs('scans')
if not os.path.exists('customer_files'):
	os.makedirs('customer_files')
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
	accountnumber = str(random.randint(100000001, 999999999))

	#creates customer directory
	if not os.path.exists(f"customer_files/{accountnumber}"):
		os.makedirs(f"customer_files/{accountnumber}")

	#writes name
	name = ImageDraw.Draw(sigcard)
	name.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 45) 
	name.text((405,387), randomname, font = name.font, fill=(0,0,0))

	#writes new account number
	account = ImageDraw.Draw(sigcard)
	account.font = ImageFont.truetype(r'C:\Windows\Fonts\Times New Roman\timesbd.ttf', 45) 
	account.text((495,423), accountnumber, font = account.font, fill=(0,0,0))
	#sigcard.save(f"created/{number}.jpg")

	#adds qr code
	if random.randrange(0,1) == 0:
		qrmessage = f"document name: signature card - account number: {str(accountnumber)} - name1: {randomname}"
		print(qrmessage + " " + str(number))
		qrcodeimg = qrcode.make(qrmessage, box_size=11)
		#qrcodeimg = qrcodeimg.resize((200,200))
		sigcard.paste(qrcodeimg, (1900,2400))
		#(2443, 3225)
	path = f"scans/scan_number_{number+1}.jpg"
	sigcard.save(path)

	if tiltSet:
		image = Image.open(path)
		image = image.rotate(random.randrange(-10,10), expand=True)
		image = image.save(path)
	



print("Done!")
exit()