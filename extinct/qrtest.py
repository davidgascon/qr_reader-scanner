import cv2
from PIL import Image
import random

qrlink = 'newestqrcode.jpg'
qrlink2 = 'newestqrcode2.jpg'
image = Image.open(qrlink)
image = image.rotate(random.randrange(0,10), expand=True)
image = image.save(qrlink2)


image = cv2.imread(qrlink2)
cv2.imshow('image', image)
cv2.waitKey(0)

#qrCD = cv2.QRCodeDetector()

msg, _, _ = cv2.QRCodeDetector().detectAndDecode(image)

print(msg)