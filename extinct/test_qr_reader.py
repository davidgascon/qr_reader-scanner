#This is a qr reader that I used to test to see what the scanner would be capable of acheiving. I used this to play with different variables and find what works and what some of the limitations would be. This script also includes a section that would rotate the image by -10 to 10 degrees to simulate a scan that went wrong. To create a new qr code, use the test_create_qr_code.py script.

#Findings. I found that it was really easy to create a qr code in this envirnoment. It should be able to pretty easily have the create_bulk_signature_cards script add a qr code to the signature card.

#After getting the qr code to work when the image was strictly a QR Code, I found that as soon as I put it onto a signature card and tried to read it, it would not read the QR code. I altered this script to find the points of the qr code, save that image, then read that image. 

import cv2
from PIL import Image
import random

qrlink = '../created/0-qr.jpg'
qrlink2 = 'newestqrcode2.jpg'
image = Image.open(qrlink)
image = image.rotate(random.randrange(0,1), expand=True)
image = image.save(qrlink2)


image = cv2.imread(qrlink2)
#qrCD = cv2.QRCodeDetector()
qrCodeDetector = cv2.QRCodeDetector()
msg2, points, _ = qrCodeDetector.detectAndDecode(image)

left = points[0].item(0)
upper = points[0].item(1)
right = points[2].item(0)
bottom = points[2].item(1)
print(left, upper, right, bottom)

qrcodeonly = Image.fromarray(image)
qrcodeonly = qrcodeonly.crop((left, upper, right, bottom))
qrcodeonly.save("qrcodeonly.jpg")

qrimage = cv2.imread("qrcodeonly.jpg")
msg, _, _ = qrCodeDetector.detectAndDecode(image)


print(f"points: {points[0]}")

#print(qrcode)



print(msg)
print(points)
cv2.imshow('image', image)
cv2.waitKey(0)