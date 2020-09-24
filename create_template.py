#create template
#used to create the basic template

#imports
from PIL import Image, ImageDraw, ImageFont
import cv2
from textwrap import wrap
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



#imagewidth = 563
#imageheight = 750

def neww(width):
	newwidth = ((width/563)*2550)
	return newwidth
def newh(height):
	newheight = ((height/750)*3300)
	return newheight
imagewidth = 2550
imageheight = 3300

template = Image.new('RGB', (imagewidth, imageheight), 'white')

#writes title
title = ImageDraw.Draw(template)
title.font = ImageFont.truetype(r'C:\Windows\Fonts\Times New Roman\timesbd.ttf', 90) 
title.text((neww(225),newh(35)), "Signature Card", font = title.font, fill=(0,0,0))

#writes name title
nametitle = ImageDraw.Draw(template)
nametitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Times New Roman\timesbd.ttf', 45) 
nametitle.text((neww(25),newh(85)), "Client Name:", font = nametitle.font, fill=(0,0,0))


#writes name
first_names_list = []
with open("misc/first_names.txt") as first_name_file:
	first_names = csv.reader(first_name_file)

	for name in first_names:
		for name in name:
			if name != '':
				first_names_list.append(name)
#print(first_names_list)

print("")
last_names_list = []
with open("misc/last_names.txt") as last_name_file:
	last_names = csv.reader(last_name_file)

	for name in last_names:
		for name in name:
			if name != '':
				last_names_list.append(name)
#print(last_names_list)

#writes name
randomname = random.choice(first_names_list) + " " + random.choice(last_names_list)
name = ImageDraw.Draw(template)
name.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 45) 
#title.text((90,86), randomname, font = name.font, fill=(0,0,0))


#writes name title
accounttitle = ImageDraw.Draw(template)
accounttitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Times New Roman\timesbd.ttf', 45) 
accounttitle.text((neww(25),newh(96)), "Account Number:", font = accounttitle.font, fill=(0,0,0))




#writes account disclosures title
disclosuretitle = ImageDraw.Draw(template)
disclosuretitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Times New Roman\timesbd.ttf', 45) 
disclosuretitle.text((neww(291),newh(148)), "Account Disclosures", font = disclosuretitle.font, fill=(0,0,0))


#writes disclosure content
disclosuretext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In cursus turpis massa tincidunt dui ut ornare lectus. Consequat interdum varius sit amet mattis vulputate enim nulla aliquet. Amet tellus cras adipiscing enim eu. Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Cras tincidunt lobortis feugiat vivamus at augue eget arcu. Volutpat maecenas volutpat blandit aliquam. Vitae tortor condimentum lacinia quis vel eros donec. Ut etiam sit amet nisl purus in mollis. Nibh sit amet commodo nulla facilisi.\nDui ut ornare lectus sit amet est placerat. Nunc faucibus a pellentesque sit amet porttitor eget dolor morbi. Eu facilisis sed odio morbi quis commodo. Arcu cursus vitae congue mauris. Pulvinar etiam non quam lacus. Dolor sit amet consectetur adipiscing elit. Aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis. Nunc eget lorem dolor sed viverra ipsum nunc aliquet bibendum. Consectetur adipiscing elit duis tristique sollicitudin nibh sit. Lectus vestibulum mattis ullamcorper velit sed ullamcorper. Velit ut tortor pretium viverra suspendisse. Sit amet consectetur adipiscing elit pellentesque. Tellus id interdum velit laoreet id donec ultrices. Felis bibendum ut tristique et egestas. Elementum integer enim neque volutpat. Amet consectetur adipiscing elit pellentesque. Eget lorem dolor sed viverra ipsum. Consectetur adipiscing elit duis tristique."
disclosuretextarray = wrap(disclosuretext, width=57)
print(disclosuretextarray)
disclosure = ImageDraw.Draw(template)
disclosure.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 45) 
row = 0
for text in disclosuretextarray:
	title.text((neww(291),newh(165+(row*10))), text, font = disclosure.font, fill=(0,0,0))
	row += 1

#writes signature title
signaturetitle = ImageDraw.Draw(template)
signaturetitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constanz.ttf', 45) 
signaturetitle.text((neww(30), newh(668)), "Signature 1: ", font = signaturetitle.font, fill=(0,0,0))

signature2title = ImageDraw.Draw(template)
signature2title.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constanz.ttf', 45) 
signature2title.text((neww(30), newh(698)), "Signature 2: ", font = signature2title.font, fill=(0,0,0))



template.save('template.jpg')

template = cv2.imread("template.jpg")

border = cv2.rectangle(template, (45, 45), (2489, 3255), (0, 0, 0), 7) #draws the border
customer_information_border = cv2.rectangle(template, (85, 337), (2443, 562), (0, 0, 0), 5) #draws the border around customer information
disclosure_border = cv2.rectangle(template, (1264, 615), (2443, 2025), (0, 0, 0), 3) #draws the border around the disclosure stuff
signature_border = cv2.rectangle(template, (85, 2925), (2443, 3225), (0, 0, 0), 3) #draws the border around the disclosure stuff
signature_line = cv2.line(template, (382, 3060), (1215, 3060), (0, 0, 0), 3)
signature_line2 = cv2.line(template, (382, 3195), (1215,3195), (0, 0, 0), 3)

cv2.imwrite('template.jpg', template)

scale_percent = 20 # percent of original size
width = int(template.shape[1] * scale_percent / 100)
height = int(template.shape[0] * scale_percent / 100)
dim = (width, height)

template = cv2.resize(template, dim, interpolation = cv2.INTER_AREA)
cv2.imshow('template', template)
cv2.waitKey(0)