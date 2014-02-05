from bs4 import BeautifulSoup
import urllib2
def from_page(pageurl):
	response = urllib2.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	p=soup.find_all('td',class_="image")
	
	for i in p:
		lnk=i.contents[1]['href']
		#f.write()
		with open("2008list.txt", "a") as myfile:
			myfile.write(lnk.split('/')[2]+'\n')


		

url="http://www.imdb.com/search/title?year=2008,2008&title_type=feature&sort=moviemeter,asc"
response = urllib2.urlopen(url)
page_source = response.read()
soup = BeautifulSoup(page_source)
p=soup.find_all('span',class_="pagination")
from_page('http://www.imdb.com/search/title?year=2008,2008&title_type=feature&sort=moviemeter,asc')
for i in range(113):
	response = urllib2.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	p=soup.find_all('span',class_="pagination")
	new=p[0].contents[-2]['href']
	print new
	url="http://www.imdb.com/"+new
	from_page(url)

