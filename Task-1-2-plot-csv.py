## plot task 1 - Homework 3 - CS518 computer vision ##
## Mahdi Ali pour

import os
import csv
import numpy as np
import matplotlib.pyplot as plt


#### Extracting subdirectories and count existing images for each ######

datasetPath = 'veri5_fused/type/'
csv_file_name = 'pollentype.csv'
#### ploting created CSV  ##############################################

x = []
y = []
  
with open(csv_file_name,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[1])
        y.append(int(row[0]))
  
plt.bar(x, y, color = 'g', width = 0.1, label = "Number")
plt.xlabel('Type')
plt.xticks(rotation = 45 , fontsize = 6) # Rotates X-Axis Ticks by 45-degrees
plt.ylabel('Qty')
plt.title('The number images for each type')
plt.legend()
plt.show()
