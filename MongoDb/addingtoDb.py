import pymongo
import json
import os
dirs="/home/vr/Main_Project/Yearwise/2001/data/"

con=pymongo.Connection('localhost',27017)
filmdb=con.filmsDb
col_01=filmdb.my_col

# for jfile in os.listdir(dirs):
# 	with open(dirs+jfile) as data_file:
# 		data = json.load(data_file)
# 		col_01.insert(data)
print col_01.find({"BoxOffice":"N/A"}).count()
for i in list(col_01.find({"BoxOffice":"N/A"})):
	print i["Title"].encode('ascii', 'ignore') #to avoid ascii error
