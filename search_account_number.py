#reads the file in created folder, then outputs the account number if found. 

#notes
#originally I used an image size of 563px x 750px for the template because that is what I googled the pixel dimentions would be that would result in a 'good enough' image size for this project. I learned when I started this script that when the image size was not high enough. I crated 5 signature cards using random numbers and the template I had at the time (sized 563x750). I converted the image to a string using tesseract, then tried to find "signature card" and "account number" in the returned screen. I found that it found 5 instances where siganture card was returned, but only 3-4 account numbers were returned. I did some searching and found that I learned I should've increased the size for a higher DPI, which was something I considered when I began, but figured it wouldn't be an issue. I was wrong. To view this testing script, it is stored in the extinct folder as 'signatureandaccountcount.py'


import os

from PIL import Image

import pytesseract

import re

import cv2

#tesseract path
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'

tesseractscans = 0
qrscans = 0
not_converted_total = 0

#checks for the created folder, if it doesn't create it
if not os.path.exists('not_converted'):
    os.makedirs('not_converted')

if len(os.listdir("scans/")) > 0 :
	for file in os.listdir("scans/"): #for file in created folder
		print("Checking new sig document.")
		#search for QR Code
		image = cv2.imread('scans/' + file) #read the file
		ogmsg, points, _ = cv2.QRCodeDetector().detectAndDecode(image) #returns the message and a list of cordinates of where the qr code is. If none, then there's no qr code
		if points is not None:
			try:
				#cleans account number
				msg = ogmsg.replace(" ", "")
				print(f"QR Message is:{msg}")
				msg = msg.split("accountnumber:")
				
				msg = msg[1]
				msg = msg.split("-")
				msg = msg[0]
				print(msg)
				accountnumber = msg
				qrscans = qrscans + 1
				tesseractread = False

				#cleans document type
				doctype = ogmsg.replace(" ", "")
				doctype = doctype.split("documentname:")
				doctype = doctype[1]
				doctype = doctype.split("-")
				doctype = doctype[0]
				print(doctype)
				reader_status = 'success'

			except:
				
				print("Error with reading QR Code.")
				tesseractread = True
		else:
			tesseractread = True


		if tesseractread == True:
			try:
				print("tesseract reading document")
			
				#searches document for Account Number
				img = Image.open('scans/' + file)
				string = pytesseract.image_to_string(img, config='--psm 1') #


				string = string.split("Account Number:")
				accountnumber = re.findall('[0-9]+', string[1])
				accountnumber = accountnumber[0]
				print(f"Account number for this card is {accountnumber}")
				tesseractscans = tesseractscans + 1
				reader_status = 'success'
			except:
				print("Error reading tesseract scans. Try to improve your scan quality or manually move file.")
				reader_status = 'failure'
				accountnumber = 0

		

		if int(accountnumber) > 10000 and reader_status == 'success' :
			img = Image.open('scans/' + file)
			img.save(f"customer_files/{accountnumber}/signature_card.jpg")
			os.remove(f"scans/{file}")
		else:
			img = Image.open('scans/' + file)
			img.save(f"not_converted/{accountnumber}.jpg")
			os.remove(f"scans/{file}")
			not_converted_total = not_converted_total + 1

		print("\n")
else:
	print("No scans to read!")
print(f"Scans not converted: {not_converted_total}")
print(f"Tesseract Scans: {tesseractscans}")
print(f"QR Scans: {qrscans}")