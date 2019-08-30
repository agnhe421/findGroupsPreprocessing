import csv
import os
from collections import defaultdict
dataPath = "/Users/agnesheppich/Documents/School/tnm098/findGroupsPreprocessing/parsed/friday.csv"
families = []
data = []
print("Reading data...")

with open(dataPath) as f:
    reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId', 'GroupSize']) 
    next(reader)   
    for row in reader:
        if float(row['GroupSize']) > 1: 
            families.append(row)
        
print('Family? ')
print(families)

# with open('groupSizes/groupSizesSunday', 'w') as outfile:
#     out = csv.DictWriter(outfile, fieldnames = ["alone", "twoToThree", "threeToFour", "moreThanFour"])
#     out.writeheader()
#     for test in data: 
#         outfile.write(str(test))
#         outfile.write(',')
#     outfile.close()	
