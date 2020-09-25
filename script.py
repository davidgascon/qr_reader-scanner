#script
import os
import cv2


print("Welcome to the signature reader!")

os.system('create_bulk_signature_cards.py')

input("We have created the signature cards. They are stored in the folder labeled 'scans'. Notice how the customer_files folder has all of the account numbers, but the new signature cards that were just created do not have any files. Lets put the scans in their respective customer folders. Press enter to start the sorting script.")
os.system('search_account_number.py')

print("Great! We've sorted as many as we could, , put the ones I could not read in the folder named 'not_converted', and removed them from the scans folder!")
input("That's all for today! Press enter to exit.")
exit()

