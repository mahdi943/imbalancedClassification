## task 1 - Homework 3 - CS518 computer vision ##
## Mahdi Ali pour

import os
import csv
import numpy as np


#### Extracting subdirectories and count existing images for each ######

datasetPath = 'veri5_fused/type/'
csv_file_name = 'pollentype2.csv'

x = os.scandir(datasetPath)
for item in x:
    arr = []
    _, _, files = next(os.walk(item.path))
    file_count = len(files)
    print('Number of images: ',file_count, 'Name: ', item.name)
    arr.append(str(file_count))
    arr.append(item.name)

#### Save count and types name into a CSV for further usage ############     
    with open(csv_file_name, 'a', newline = '') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ',')
        my_writer.writerow(arr)

print("Done! \nData is saved in ", csv_file_name )

 

