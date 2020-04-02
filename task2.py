import pandas as pd
import re
import json

#Reading the files using standard python libraries.

file1 = input('Enter the name of csv file: ')
file2 = input('Enter the name of the json file: ')

with open(file2) as f:
    data = json.load(f)

#Reading the csv file while using only 3 columns out of 4.

df = pd.read_csv(file1, usecols = ['Name', 'Organisation', 'Project'])

#Creating a new list for storing names so as to work upon them separately.
names = []

for name in df["Name"]:
    names.append(name)

#Creating a new list after removing the names which are not allowed.
accept_names = []

#A function for checking the presence of a digit in the given string.
def hasNumbers(inputString):
   return any(char.isdigit() for char in inputString)

#names.append(" Mark")

#Looping through the name list and checking for the allowed names by setting a flag to 1 if the string is not allowed.
print("The list of invalid students consists: ")
for name in names:
    flag = 0
    #Condition to check the presence of a number or a special symbol.
    if ((not(re.match("^[a-zA-Z ]*$", name))) or (hasNumbers(name))):
        flag = 1
    #Condition to check the presence of just lowe-case letters.
    if (re.match('^[a-z]+$', name)):
        flag = 1
    #Condition for the presence of two words.
    if (name.find(" ") == -1):
        flag = 1
    #Condition to check if the starting of the name is with a space as such a name has only word but bypasses all the above tests.
    if (name[0] == ' '):
        flag = 1
    if (flag == 1):
        print(name)
    else: 
        accept_names.append(name)

#Looping over the names in json file and checking if the name is present in accepted names.
print("The details of the people who were matched is : ")
for student in data:
    count = 0
    flag = 0
    if (student["n"] in accept_names):
        rollno = student["i"]
        branch = student["d"]
        name = student["n"]
        for person in df["Name"]:
            if (person == student["n"]):
                organisation = df["Organisation"].iloc[count]
                project = df["Project"].iloc[count]
                flag = 1
            if (flag):
                break
            else:
                count += 1
        print ("Name:", name, "Roll No:", rollno, "Branch:", branch, organisation, "Project:", project)
