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

imagewidth = 563
imageheight = 750

template = Image.new('RGB', (imagewidth, imageheight), 'white')

#writes title
title = ImageDraw.Draw(template)
title.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constanz.ttf', 20) 
title.text((225,35), "Signature Card", font = title.font, fill=(0,0,0), size=20)

#writes name title
nametitle = ImageDraw.Draw(template)
nametitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constanz.ttf', 10) 
nametitle.text((25,85), "Client Name:", font = nametitle.font, fill=(0,0,0))


#writes name title
name = ImageDraw.Draw(template)
name.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 10) 
title.text((90,86), "David Gascon", font = name.font, fill=(0,0,0))


#writes name title
accounttitle = ImageDraw.Draw(template)
accounttitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constanz.ttf', 10) 
accounttitle.text((25,96), "Account Number:", font = accounttitle.font, fill=(0,0,0))


#writes account title
account = ImageDraw.Draw(template)
account.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 10) 
title.text((110,94), str(random.randint(100000001, 999999999)), font = account.font, fill=(0,0,0))

#writes name title
disclosuretitle = ImageDraw.Draw(template)
disclosuretitle.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constanz.ttf', 10) 
disclosuretitle.text((291,140), "Account Disclosures", font = disclosuretitle.font, fill=(0,0,0))


#writes disclosure title
disclosuretext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In cursus turpis massa tincidunt dui ut ornare lectus. Consequat interdum varius sit amet mattis vulputate enim nulla aliquet. Amet tellus cras adipiscing enim eu. Sit amet mattis vulputate enim nulla aliquet porttitor lacus luctus. Cras tincidunt lobortis feugiat vivamus at augue eget arcu. Volutpat maecenas volutpat blandit aliquam. Vitae tortor condimentum lacinia quis vel eros donec. Ut etiam sit amet nisl purus in mollis. Nibh sit amet commodo nulla facilisi.\nDui ut ornare lectus sit amet est placerat. Nunc faucibus a pellentesque sit amet porttitor eget dolor morbi. Eu facilisis sed odio morbi quis commodo. Arcu cursus vitae congue mauris. Pulvinar etiam non quam lacus. Dolor sit amet consectetur adipiscing elit. Aliquam eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis. Nunc eget lorem dolor sed viverra ipsum nunc aliquet bibendum. Consectetur adipiscing elit duis tristique sollicitudin nibh sit. Lectus vestibulum mattis ullamcorper velit sed ullamcorper. Velit ut tortor pretium viverra suspendisse. Sit amet consectetur adipiscing elit pellentesque. Tellus id interdum velit laoreet id donec ultrices. Felis bibendum ut tristique et egestas. Elementum integer enim neque volutpat. Amet consectetur adipiscing elit pellentesque. Eget lorem dolor sed viverra ipsum. Consectetur adipiscing elit duis tristique."
disclosuretextarray = wrap(disclosuretext, width=57)
print(disclosuretextarray)
disclosure = ImageDraw.Draw(template)
disclosure.font = ImageFont.truetype(r'C:\Windows\Fonts\Constantia\constani.ttf', 10) 
row = 0
for text in disclosuretextarray:
	title.text((291,150+(row*10)), text, font = disclosure.font, fill=(0,0,0))
	row += 1




template.save('template.jpg')

template = cv2.imread("template.jpg")

border = cv2.rectangle(template, (10,10), (553, 740), (0, 0, 0), 2) #draws the border
customer_information_border = cv2.rectangle(template, (20, 75), (543, 125), (0, 0, 0), 1) #draws the border around customer information
disclosure_border = cv2.rectangle(template, (281, 130), (543, 450), (0, 0, 0), 1) #draws the border around the disclosure stuff

cv2.imwrite('template.jpg', template)
cv2.imshow('template', template)
cv2.waitKey(0)