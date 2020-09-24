# qr_reader-scanner
Notes:

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


Steps to develop.
1. Create a way to create a blank signature card (PIL) (done)
2. Create a way to create (insert number here) number of 'fake' signature cards including some distortion to replicate a real scan. Save them in a folder. Also add a checkbox to add qr code/barcode

3. Figure out how to scan each file, then move file to appropriate folder.
3.1 If no barcode/qr code, search for account number (Partially done)

