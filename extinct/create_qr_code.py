#used to test creating a qr code

import qrcode
import random
#from PIL import Image

message = "hey! This is a new test number " + str(random.randrange(0,50)) + ". The account number is " + str(random.randrange(1000,9999))
img = qrcode.make(message)
img.save("newestqrcode.jpg")
