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

print("Finding the group...")

with open(dataPath) as f:
	reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y']) 
	for row in reader:
		#Find the people who have checked in at the same place in the same time
		if(row['type'] == 'check-in'):
			data.append(row)
			
for i in range (0, len(data)): 
	if(i+1 < len(data)):
		if(data[i]['X'] == data[i+1]['X'] and data[i]['Y'] == data[i+1]['Y'] and data[i]['TimeStamp'] == data[i+1]['TimeStamp']):	
			print('Family or small group, saving data...')
			#print(data[i])
			group.append(data[i])

		outputDataFile = open(fileNameString, 'a')

			# with open(generatedDataDir + 'parsedDataFile', 'w') as w:
			# 	writer = csv.writer(w)
			# 	writer.writerows(data[i])

			# w.close()

for i in range(0, len(group)):
	print(group[i])

print('Finished!')

