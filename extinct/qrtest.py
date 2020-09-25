import cv2
from PIL import Image

image = Image.open('testqr.png')
image = image.rotate(10, expand=True)
image = image.save('testqr2.png')


image = cv2.imread('testqr2.png')
cv2.imshow('image', image)
cv2.waitKey(0)

qrCD = cv2.QRCodeDetector()

msg, g, f = qrCD.detectAndDecode(image)

print(msg)