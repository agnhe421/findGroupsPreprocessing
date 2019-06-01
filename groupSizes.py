import csv
import os
from collections import defaultdict

dataPath = "C:/tnm098/preprocessing/findGroupsPreprocessing/parsed/fridayTest.csv"
alone = []
twoToThree = []
threeToFour = []
moreThanFour = []
data = []
print("Reading data...")

with open(dataPath) as f:
    reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId', 'GroupSize']) 
    for row in reader:
        if float(row['GroupSize']) > 0 and float(row['GroupSize']) < 2: 
            alone.append(row['GroupSize'])
        if float(row['GroupSize']) > 1 and float(row['GroupSize']) < 3: 
            twoToThree.append(row['GroupSize'])
        if float(row['GroupSize']) > 2 and float(row['GroupSize']) < 5: 
            threeToFour.append(row['GroupSize'])
        if float(row['GroupSize']) > 4: 
            moreThanFour.append(row['GroupSize'])
    
print('Group sizes: ')

aloneSize = len(alone)
twoToThreeSize = len(twoToThree)
threeToFourSize = len(threeToFour)
moreThanFourSize = len(moreThanFour)

data.append(aloneSize)
data.append(twoToThreeSize)
data.append(threeToFourSize)
data.append(moreThanFourSize)

print(data)
with open('groupSizes/groupSizes', 'w') as outfile:
    out = csv.DictWriter(outfile, fieldnames = ["alone", "twoToThree", "threeToFour", "moreThanFour"])
    out.writeheader()
    for test in data: 
        outfile.write(str(test))
        outfile.write(',')
    outfile.close()	
