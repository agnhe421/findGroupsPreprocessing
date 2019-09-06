import csv
import os
from collections import defaultdict
from datetime import datetime
import time
# dataPath = "/Users/agnesheppich/Documents/School/tnm098/findGroupsPreprocessing/parsed/friday.csv"
dataPath = "/Users/agnesheppich/Documents/School/tnm098/findGroupsPreprocessing/data/friday.csv"
printToFile = 'earlyBirdsFriday'

groups = []
data = []
print("Reading data...")

earlyBirdsInFriday = 1402048800 #12pm
earlyBirdsInSaturday = 1402135200
earlyBirdsInSunday = 1402221600

with open(dataPath) as f:
    reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId']) 
    next(reader)   
    for row in reader:
        if(row['type'] == 'check-in'):
            d = datetime.strptime(row['TimeStamp'], '%Y-%m-%d %H:%M:%S')
            timeStampInSeconds = time.mktime(d.timetuple())
            
            if(
                # (timeStampInSeconds > earlyBirdsInFriday)):
                (timeStampInSeconds > earlyBirdsInSaturday)):
                # (timeStampInSeconds > earclyCheckInSunday)): 
                groups.append(row)
        

numberOfPeople = 0
individualIds = []
ids = []

#Filter away all duplicate ids
for i in range (0, len(groups)): 
    ids.append(groups[i]['id'])
ids = list(dict.fromkeys(ids))

for j in range(0, len(ids)): 
    print(ids[j])

print(len(ids))

with open('parsed/' + printToFile, 'w') as outfile:
    fp = csv.DictWriter(outfile, groups[0].keys())
    fp.writeheader()
    fp.writerows(groups)
    outfile.close()	