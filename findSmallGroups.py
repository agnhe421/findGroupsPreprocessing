import csv
import os
from collections import defaultdict

localPath = "C:/tnm098/preprocessing/"
generatedDataDir = "parsed/"
dataFile = "friday.csv"
dataDir = "data/"
dataExtension = ".csv"

dataPath = localPath + dataDir + dataFile

print("Finding the group...")

with open(dataPath) as f:
	reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y']) 
	for row in reader:
		print('Timestamp: ' + row['TimeStamp'] + 'id: ' + row['id'])
