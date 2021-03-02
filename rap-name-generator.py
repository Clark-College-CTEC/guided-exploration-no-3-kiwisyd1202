# Guided Exploration No. 3
# Sydney Henwood

import random  # this imports the python random library

possible_names = []  # creates an empty list named possible_names

outputFile = open('rap-names-output.txt', 'w')  # opens a new file named rap-names-output.txt, which is going to be written in

with open('rap-names.txt', 'r') as dataFile:  # opens rap-names.txt for read access, assigns the handle dataFile to it
    for name in dataFile:  # loop that iterates through each line in rap-names.txt
        possible_names.append(name.rstrip())  # reads line from rap-names.txt and strips off the line feed to the right, appends that to possible_names list


count = int(input('How many rap names would you like to create? '))  # asks the user to input how many rap names to create, assigns that number to variable count
parts = int(input('How many parts should the name contain? '))  # asks the user to input how many parts each name should have, assigns that number to variable parts


for i in range(count):  # runs this loop {count} times
    name_parts = []  # creates list to hold rap name parts
    for j in range(parts):  # runs this loop {parts} times
        # randomly selects name from possible_names, appends it to name_parts list
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])
    outputFile.write(f"{' '.join(name_parts)}\n")  # writes the names into the file, each word seperated with a space, with a line feed at the end
    print(f"{' '.join(name_parts)}")  # prints out the new rap name
outputFile.close()  # closes the rap-names-output.txt file
