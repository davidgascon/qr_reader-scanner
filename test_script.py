#reads the file in created 

#notes
#originally I used an image size of 563px x 750px for the template because that is what I googled the pixel dimentions would be that would result in a 'good enough' image size for this project. I learned when I started this script that when the image size was not high enough. I crated 5 signature cards using random numbers and the template I had at the time (sized 563x750). I converted the image to a string using tesseract, then tried to find "signature card" and "account number" in the returned screen. I found that it found 5 instances where siganture card was returned, but only 3-4 account numbers were returned. I did some searching and found that I learned I should've increased the size for a higher DPI, which was something I considered when I began, but figured it wouldn't be an issue. I was wrong. To view this testing script, it is stored in the extinct folder as 'signatureandaccountcount.py'


import os

from PIL import Image

import pytesseract

import re


#tesseract path
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tesseract.exe'
counter = 0
signaturecounter = 0
accountcounter = 0
for file in os.listdir("scans/"): #for file in created folder
	img = Image.open('scans/' + file)
	string = pytesseract.image_to_string(img, config='--psm 1')
	string.replace(" ", "")
	#print(string)
	if "Signature" in string:
		signaturecounter = signaturecounter + 1
	if "Account Number" in string:
		accountcounter = accountcounter + 1
	if "884752288" in string:
		counter = counter + 1
	#print(f"Signautres: {signaturecounter}")
	#print(f"account numbers: {accountcounter}")
	#print(f"884752288 found {counter} times")
	string = string.split("Account Number:")
	accountnumber = re.findall('[0-9]+', string[1])
	print(f"Account number for this card is {accountnumber[0]}")