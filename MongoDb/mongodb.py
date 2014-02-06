import pymongo

con=pymongo.Connection('localhost',27017)
filmdb=con.filmsDb
col_01=filmdb.my_col

print col_01.find({"BoxOffice":"N/A"}).count()
for i in list(col_01.find({"BoxOffice":"N/A"})):
	print i["imdbID"].encode('ascii', 'ignore') #to avoid ascii error

