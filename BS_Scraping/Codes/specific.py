from bs4 import BeautifulSoup
import urllib2

		


def form_film(ttid):
	url='http://www.imdb.com/title/'+ttid
	response = urllib2.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	Title=soup.find_all('span',class_="itemprop",itemprop="name")
	titl= Title[0].string # title.
	Desc=soup.find_all('p',itemprop="description")[0].string.split('\n')[1]
	Director= soup.find_all('div',itemprop="director")[0].contents[3].string 
	Actorslst=soup.find_all('div',itemprop="actors")[0].find_all('a')
	for i in Actorslst:
		print i.string
	#with open(ttid+titl, "a") as myfile:
			#myfile.write("Title :"+titl+'\n')
			#myfile.write("Description :"+Desc+'\n')
			#myfile.write("Director :"Director+'\n')
	 
form_film('tt0209958') 
			

