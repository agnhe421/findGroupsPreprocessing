import csv
import os
from collections import defaultdict
from datetime import datetime
import time

dataPath = "/Users/agnesheppich/Documents/School/tnm098/findGroupsPreprocessing/data/sunday.csv"
printToFile = 'morningSunday'

groups = []
data = []
print("Reading data...")

TwelvePmFriday = datetime.strptime('2014-6-06 12:00:00', '%Y-%m-%d %H:%M:%S')
TwelvePmFridayInSeconds = time.mktime(TwelvePmFriday.timetuple())

TwelvePmSaturday = datetime.strptime('2014-6-07 12:00:00', '%Y-%m-%d %H:%M:%S')
TwelvePmSaturdayInSeconds = time.mktime(TwelvePmSaturday.timetuple())

TwelvePmSunday = datetime.strptime('2014-6-08 12:00:00', '%Y-%m-%d %H:%M:%S')
TwelvePmSundayInSeconds = time.mktime(TwelvePmSunday.timetuple())


SixPmFriday = datetime.strptime('2014-6-06 18:00:00', '%Y-%m-%d %H:%M:%S')
SixPmFridayInSeconds = time.mktime(SixPmFriday.timetuple())

SixPmSaturday = datetime.strptime('2014-6-07 18:00:00', '%Y-%m-%d %H:%M:%S')
SixPmSaturdayInSeconds = time.mktime(SixPmSaturday.timetuple())

SixPmSunday = datetime.strptime('2014-6-08 18:00:00', '%Y-%m-%d %H:%M:%S')
SixPmSundayInSeconds = time.mktime(SixPmSunday.timetuple())

with open(dataPath) as f:
    reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId']) 
    next(reader)   
    for row in reader:
        if(row['type'] == 'check-in'):
            d = datetime.strptime(row['TimeStamp'], '%Y-%m-%d %H:%M:%S')
            timeStampInSeconds = time.mktime(d.timetuple())
            print('time in seconds: ' + str(timeStampInSeconds))
            if (
                # (timeStampInSeconds < TwelvePmFridayInSeconds)):
                # (timeStampInSeconds < TwelvePmSaturdayInSeconds)):
                (timeStampInSeconds < TwelvePmSundayInSeconds)): 
                groups.append(row)
            # if (
                # (timeStampInSeconds > TwelvePmFridayInSeconds and timeStampInSeconds < SixPmFridayInSeconds)):
                # (timeStampInSeconds > TwelvePmSaturdayInSeconds and timeStampInSeconds < SixPmSaturdayInSeconds)):
                # (timeStampInSeconds > TwelvePmSundayInSeconds and timeStampInSeconds < SixPmSundayInSeconds)):
                # groups.append(row)
            # if (
                # (timeStampInSeconds > SixPmFridayInSeconds)):
                # (timeStampInSeconds > SixPmSaturdayInSeconds)):
                # (timeStampInSeconds > SixPmSundayInSeconds)):

                # groups.append(row)

numberOfPeople = 0
individualIds = []
ids = []

#Filter away all duplicate ids
for i in range (0, len(groups)): 
    ids.append(groups[i]['id'])
ids = list(dict.fromkeys(ids))

# for j in range(0, len(ids)): 
    # print(ids[j])

print('total: ' + str(len(ids)))

with open('parsed/' + printToFile, 'w') as outfile:
    fp = csv.DictWriter(outfile, groups[0].keys())
    fp.writeheader()
    fp.writerows(groups)
    outfile.close()	