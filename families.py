import csv
import os
from collections import defaultdict
from datetime import datetime
import time
dataPath = "/Users/agnesheppich/Documents/School/tnm098/findGroupsPreprocessing/parsed/friday.csv"
printToFile = 'familiesFriday'
families = []
data = []
print("Reading data...")

#start = 8am, end = 12pm 
fridayStart = 1402034400
saturdayStart = 1402120800
sundayStart = 1402207200

fridayEnd = 1402048800
saturdayEnd = 1402135200
sundayEnd = 1402221600

with open(dataPath) as f:
    reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId', 'GroupSize']) 
    next(reader)   
    for row in reader:
        if float(row['GroupSize']) > 2 and float(row['GroupSize']) < 8: 
            #people who only checked in in the kids area 
            if (float(row['X'])  > 55 and float(row['Y']) > 60): 
                #Look for people who checked into the park early and didn't stay late
                d = datetime.strptime(row['TimeStamp'], '%Y-%m-%d %H:%M:%S')
                timeStampInSeconds = time.mktime(d.timetuple())
                if((timeStampInSeconds > fridayStart and timeStampInSeconds < fridayEnd) 
                or (timeStampInSeconds > saturdayStart and timeStampInSeconds < saturdayEnd)
                or (timeStampInSeconds > sundayStart and timeStampInSeconds < sundayEnd)): 
                   families.append(row)
        

numberOfPeopleVisitingInAFamily = 0; 
for i in range(0, len(families)): 
    print(families[i])
    numberOfPeopleVisitingInAFamily = numberOfPeopleVisitingInAFamily + int(families[i]['GroupSize'])

print(len(families))
print(numberOfPeopleVisitingInAFamily)

with open('parsed/' + printToFile, 'w') as outfile:
    fp = csv.DictWriter(outfile, families[0].keys())
    fp.writeheader()
    fp.writerows(families)
    outfile.close()	