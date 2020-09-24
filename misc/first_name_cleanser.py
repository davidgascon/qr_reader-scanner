#used to clean the data from the original first names csv.
#initially I used pandas, but I quickly learned it would be easy to work with the csv file rather than the data type that pandas imported it as. I realized this when I tried to clean each name.
#The main difference between this and last name cleanser is how the names were initially stored and the seperators in the csv's.

import csv

first_names_clean = [] #creates list of clean names
with open('first_names.csv') as csvfile: #opens file
	first_names = csv.reader(csvfile) #reads csv
	print(first_names)
	for name in first_names: #for each row
		for item in name: #for each item in the row
			if item != '': #if the name is not blank, append the clean name list
				first_names_clean.append(item)

print(first_names_clean)

#saves the file as a txt
file = open("first_names.txt", "w+")
for item in first_names_clean:
	file.write(f"{item},")
file.close()