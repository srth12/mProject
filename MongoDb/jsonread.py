import json
import os
dirs="/home/vr/Main_Project/Yearwise/2001/data/"
print len(os.listdir(dirs))
with open(dirs+'test0.txt') as data_file:    
    data = json.load(data_file)
print(data.values())