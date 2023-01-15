## plot family task 1 - Homework 3 - CS518 computer vision ##
## Mahdi Ali pour

import os
import csv
import numpy as np
import matplotlib.pyplot as plt


#### Extracting subdirectories and count existing images for each ######

csv_file_name = 'pollentype.csv'
csv_file_family = 'labels.csv'

#### Matching types to their family ###################################

##
##
##exist = read a line from family (filter . and take 2 first words) search it in type
##while eof family csv:
##    if not exist:
##        family_count = 0
##    exist = read a line from family search it in type
##    
##    while (not exist)
##        family count = family + type_count
##        exist = read a line from family search it in type
##    write family_count in csv
##
##'''

types = {}

with open(csv_file_name,'r') as csvfile:
    family_obj = csv.reader(csvfile, delimiter = ',')
    for row in family_obj:
        types[row[1]] = int(row[0])


##print(types)

# Open file

allLabels = []
with open(csv_file_family,'r',encoding="utf8") as csvfile:
    family_obj = csv.reader(csvfile, delimiter = ',')
    for row in family_obj:
        allLabels.append(row[0])

print(len(allLabels))
    
labelDict = {}
i=0
for data in allLabels:
    i=i+1
    data = data.replace('.','')
    splitted = data.split()

    if len(splitted)> 2:
        data = splitted[0] + ' ' + splitted[1]
        
    labelDict[data+'_'+str(i)] = 0
    for key, value in types.items():
        if(data == key):
            labelDict[data+'_'+str(i)] = value
            break
            
print(len(labelDict))

la = []
for key, value in labelDict.items():
    if value > 0 :
        print(key)
        la.append(key)

print(len(la))
   


#### ploting created CSV  ##############################################

##x = []
##y = []
##  
##with open(csv_file_name,'r') as csvfile:
##    plots = csv.reader(csvfile, delimiter = ',')
##      
##    for row in plots:
##        x.append(row[1])
##        y.append(int(row[0]))
##  
##plt.bar(x, y, color = 'g', width = 0.1, label = "Number")
##plt.xlabel('Type')
##plt.xticks(rotation = 45 , fontsize = 6) # Rotates X-Axis Ticks by 45-degrees
##plt.ylabel('Qty')
##plt.title('The number images for each type')
##plt.legend()
##plt.show()
