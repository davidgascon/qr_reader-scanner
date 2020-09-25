# qr_reader-scanner

Watch the video I made about this script and see it working. First 2 minutes are the overview and the last 7 minutes are more in depth.
http://bit.ly/DavidGasconQRProject

Notes:

Update 3. Script.py will walk you how to use the script. Essentially you are just creating the scans (or creating the signature cards), then using tesseract and QRReader to try to put them in the correct directory. It's far from perfect, however for a quite basic, sample project, it is working as well as I can hope.
Update 2. Create_template.py and create_bulk_signature_cards.py 
search_account_number.py is used to search all files in 'created' folder for an account number. It then prints the account number and saves the image to the 'converted' folder.
Update 1. create_template.py is used to create the template image, which is used in create_bulk_signature_cards.py to create a large number of signature cards. (9/23/2020 and 9/24/2020)


Lessons learned
-Never underestimate the pixels required for a quality image.
-In the future, when working with a template, I should probably use a ratio instead of a defined position for where elements are in an image. For example, the border of the signature cards could have been something like the (.05*width, .05*height) for the top left cordinate. This will save time if the number of pixels need to be changed.
-I had issues with PIL, Image and Pillow. Aparently you can only have either Pillow and Image installed, but not PIL and Image or PIL and Pillow installed. This caused issues with Pytesseract

Things Learned this project
-Image/pixel sizing when creating images
-Tesseract reading incorrect information
-Creating images from scratch 
-Regex package


Improvements that could be worked on
-Further distorting the scans and improving the QR Code detection. 
-Adding information to the signature card to make it look more complete.
-Adding different pages which the document would scan (page 1 would go to page 1 of the document, and so on)
-Set it up on a home network to simulate more of the use case for this script
