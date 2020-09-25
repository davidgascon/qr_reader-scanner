#This is a qr reader that I used to test to see what the scanner would be capable of acheiving. I used this to play with different variables and find what works and what some of the limitations would be. This script also includes a section that would rotate the image by -10 to 10 degrees to simulate a scan that went wrong. To create a new qr code, use the test_create_qr_code.py script.

#Findings. I found that it was really easy to create a qr code in this envirnoment. It should be able to pretty easily have the create_bulk_signature_cards script add a qr code to the signature card.

import cv2
from PIL import Image
import random

qrlink = 'newestqrcode.jpg'
qrlink2 = 'newestqrcode2.jpg'
image = Image.open(qrlink)
image = image.rotate(random.randrange(-10,10), expand=True)
image = image.save(qrlink2)


image = cv2.imread(qrlink2)
cv2.imshow('image', image)
cv2.waitKey(0)

#qrCD = cv2.QRCodeDetector()

msg, _, _ = cv2.QRCodeDetector().detectAndDecode(image)

print(msg)