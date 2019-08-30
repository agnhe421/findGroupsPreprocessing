import csv
import os
from collections import defaultdict
dataPath = "/Users/agnesheppich/Documents/School/tnm098/findGroupsPreprocessing/parsed/friday.csv"
alone = []
one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
moreThanEight = []
data = []
print("Reading data...")
with open(dataPath) as f:
    reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId', 'GroupSize']) 
    next(reader)   
    for row in reader:
        if float(row['GroupSize']) == 1: 
            alone.append(row['GroupSize'])
        elif float(row['GroupSize']) == 2: 
            two.append(row['GroupSize'])
        elif float(row['GroupSize']) == 3: 
            three.append(row['GroupSize'])
        elif float(row['GroupSize']) == 4: 
            four.append(row['GroupSize'])
        elif float(row['GroupSize']) == 5:
            five.append(row['GroupSize'])
        elif float(row['GroupSize']) == 6:
            six.append(row['GroupSize'])
        elif float(row['GroupSize']) == 7:
            seven.append(row['GroupSize'])
        elif float(row['GroupSize']) == 8:
            eight.append(row['GroupSize'])
        elif float(row['GroupSize']) > 8:         
            moreThanEight.append(row['GroupSize'])
    
print('Group sizes: ')

aloneSize = len(alone)
twoSize = len(two)
threeSize = len(three)
fourSize = len(four)
fiveSize = len(five)
sixSize = len(six)
sevenSize = len(seven)
eightSize = len(eight)
moreThansixEightSize = len(moreThanEight)

data.append(aloneSize)
data.append(twoSize*2)
data.append(threeSize*3)
data.append(fourSize*4)
data.append(fiveSize*5)
data.append(sixSize*6)
data.append(sevenSize*7)
data.append(eightSize*8)
data.append(moreThansixEightSize*8)

print(data)
with open('groupSizes/groupSizesSunday', 'w') as outfile:
    out = csv.DictWriter(outfile, fieldnames = ["alone", "two", "three", "four", "five", "six", "seven", "eight", "moreThanEight"])
    out.writeheader()
    for test in data: 
        outfile.write(str(test))
        outfile.write(',')
    outfile.close()	
