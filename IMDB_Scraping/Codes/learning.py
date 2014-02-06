from bs4 import BeautifulSoup
import urllib2
url="http://www.imdb.com/search/title?year=2000,2000&title_type=feature&sort=moviemeter,asc"
response = urllib2.urlopen(url)
page_source = response.read()
soup = BeautifulSoup(page_source)
p=soup.find_all('td',class_="image")
print len(p)
print p[0].contents[2]['href']