## plot task 1 - Homework 3 - CS518 computer vision ##
## Mahdi Ali pour

import os
import csv
import numpy as np
import matplotlib.pyplot as plt


## I created pollenfamily.csv and count images manually

csv_file_name = 'pollenfamily.csv'
#### ploting created CSV  ##############################################

x = []
y = []
  
with open(csv_file_name,'r' ,encoding="utf8") as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        if row[1] !='':
            x.append(row[0])
            y.append(int(row[1]))
  
plt.bar(x, y, color = 'g', width = 0.1, label = "Number")
plt.xlabel('Family')
plt.xticks(rotation = 45 , fontsize = 8) # Rotates X-Axis Ticks by 45-degrees
plt.ylabel('Qty')
plt.title('The number images for each Family')
plt.legend()
plt.show()
