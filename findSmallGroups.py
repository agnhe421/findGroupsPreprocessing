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
	reader = csv.DictReader(f, fieldnames=['TimeStamp', 'id', 'type', 'X', 'Y']) 
	for row in reader:
		#Find the people who have checked in at the same place in the same time
		if(row['type'] == 'check-in'):
			data.append(row)
			

#MAKE SURE IT'S THE FIRST CHECK IN 
	#kolla om id:t redan finns i listan av grupper 
#FIND PEOPLE WHO CHECKED IN AT THE SAME TIME
#DELETE EVERYBODY IN THE GROUP THAT'S NOT THE FIRST PERSON 
#SAVE INFORMATION ABOUT HOW MANY PEOPLE IN THE GROUP AND CREATE A GROUP ID


for i in range(0, len(data)):
	if not(data[i]['id'] in group):
		#print('looking for groups...')

		if(i+1 < len(data)):
			if not(data[i]['X'] == data[i+1]['X'] and data[i]['Y'] == data[i+1]['Y'] and data[i]['TimeStamp'] == data[i+1]['TimeStamp'] ):
				#print(data[i])
				print('NEW member')
				print(data[i])
				group.append(data[i])
				numberOfPeopleIngroup = len(deletedMembers)
				numberOfPeopleInGroupLIst.append(numberOfPeopleIngroup)
				deletedMembers.clear()
			else:
				deletedMembers.append(data[i])
				print('member DELETED')
				print(data[i])
		#print('next dataline')

for x in range(0, len(group)):
	print(group[x])
for y in range (0, len(numberOfPeopleInGroupLIst)):
	print(numberOfPeopleInGroupLIst[y])






	#print(data[i])
			#elif(data[i]['X'] == data[i+1]['X'] and data[i]['Y'] == data[i+1]['Y'] and data[i]['TimeStamp'] == data[i+1]['TimeStamp'] ):

# for i in range (0, len(data)): 
# 	if(i+1 < len(data)):
# 		#People who checked in at the same time position as at least one other person

# 		if(data[i]['X'] == data[i+1]['X'] and data[i]['Y'] == data[i+1]['Y'] and ):#and data[i]['TimeStamp'] == data[i+1]['TimeStamp']):	
# 			if(data[i]['TimeStamp'] == data[i+1]['TimeStamp']):
# 				print('same timestamp')
# 				# print(data[i])
# 				#print('Same timestamp')
# 				#print(data[i])
# 				group.append(data[i])
# 				#print(data[i])

# 			else: 
# 			 	print('NOT the same timestamp')
# 			# 	print(data[i])

# 		# if not(data[i]['X'] != data[i+1]['X'] or data[i]['Y'] != data[i+1]['Y'] or data[i]['TimeStamp'] != data[i+1]['TimeStamp']):
# 		# 	group.append(data[i])
# 		# 	#print(data[i])


# for i in range(0, len(group)):
# 	print(group[i])

#print('Finished!')

