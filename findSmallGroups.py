import csv
import os
from collections import defaultdict

localPath = "C:/tnm098/preprocessing/findGroupsPreprocessing/"
generatedDataDir = "parsed/"
dataFile = "testData.csv"
dataDir = "data/"
dataExtension = ".csv"

parsedDataFile = "Friday"
dataPath = localPath + dataDir + dataFile

group = []
data = []
deletedMembers = []
numberOfPeopleInGroupLIst = []

print("Finding the group...")

with open(dataPath) as f:
	reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y', 'GroupId', 'GroupSize']) 
	for row in reader:
		#Find the people who have checked in at the same place in the same time
		if(row['type'] == 'check-in'):
			data.append(row)
		

for i in range(0, len(data)):
	if not(data[i]['id'] in group):
		#print('looking for groups...')
		if(i+1 < len(data)):
			if not(data[i]['X'] == data[i+1]['X'] and data[i]['Y'] == data[i+1]['Y'] and data[i]['TimeStamp'] == data[i+1]['TimeStamp'] ):
				#print(data[i])
				#print('NEW member')
				group.append(data[i])
				numberOfPeopleIngroup = len(deletedMembers)
				numberOfPeopleInGroupLIst.append(numberOfPeopleIngroup)
				deletedMembers.clear()
				data[i]['GroupSize'] = groupSize + 1
				#print(data[i])
				groupSize = 0

			else:
				deletedMembers.append(data[i])
				groupSize = len(deletedMembers)
				#print(groupSize); 
				data[i]['GroupSize'] = groupSize + 1
				#print('member DELETED')
		#		print(data[i])
		#print('next dataline')

for x in range(0, len(group)):
# 	print(group[x])
	group[x]['GroupId'] = x
	#print(group[x])

	# with open(..., 'wb', newline='') as myfile:
    #  wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #  wr.writerow(mylist)



with open('parsed/parsedDataFile', 'w') as outfile:
    fp = csv.DictWriter(outfile, group[0].keys())
    fp.writeheader()
    fp.writerows(group)
    outfile.close()	