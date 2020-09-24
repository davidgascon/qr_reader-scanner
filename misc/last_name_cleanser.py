#used to clean the data from the original last names csv.
#initially I used pandas, but I quickly learned it would be easy to work with the csv file rather than the data type that pandas imported it as. I realized this when I tried to clean each name.
#The main difference between this and first name cleanser is how the names were initially stored and the seperators in the csv's.


import csv 
clean_last_names = [] #creates a list of clean last names
with open('original_last_names.csv') as csvfile: #opens the file
	last_names = csv.reader(csvfile) #reads the file
	print(last_names)
	for name in last_names: #the inital rows are formatted like 1. Gascon . For each row
		name = str(name) #Sets the datatype for that row to a string rather than a list item
		name = name.split(" ") #The spaces are between the period and the first character of each name. Split the name here. name[1] should be the last name. Right now we have something close to Gascon'] . the '] comes from changing the row to a string
		name = name[1] #sets the name we're working with to the second half of the split. It's just easier for me to do this. I bet I could've combined this with the above line if I tried hard enough
		name = name.split("'") #since our strings are now Gascon'] , split the string at the '. 
		print(name[0]) #we really only care about the first half of the split
		clean_last_names.append(name[0]) #add to the clean list
		
	print(name)

print(clean_last_names)

#writes the list to a txt file.
file = open("last_names.txt", "w+")
for item in clean_last_names:
	file.write(f"{item},")
file.close()