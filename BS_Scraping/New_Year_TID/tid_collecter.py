from bs4 import BeautifulSoup
import urllib2


def from_page(pageurl,year):#To find all TID in a ginven page
	fname=str(year)+"list.txt"
	response = urllib2.urlopen(pageurl)
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	p=soup.find_all('td',class_="image")
	
	for i in p:
		lnk=i.contents[1]['href']
		#f.write()
		with open(fname, "a") as myfile:
			myfile.write(lnk.split('/')[2]+'\n')


		
def from_year(year):#To find all pages in a given year
	url="http://www.imdb.com/search/title?year=%d,%d&title_type=feature&sort=moviemeter,asc"%(year,year)
	response = urllib2.urlopen(url)
	page_source = response.read()
	soup = BeautifulSoup(page_source)
	p=soup.find_all('span',class_="pagination")
	from_page(url,year) #initial page
	no_of_flims=soup.find_all('div',id="left")[0].contents[0].split()[2]
	no_str=no_of_flims.split(',')[0]+no_of_flims.split(',')[1]
	no=int(no_str)/50 #remining pages
	for i in range(no):
		response = urllib2.urlopen(url)
		page_source = response.read()
		soup = BeautifulSoup(page_source)
		p=soup.find_all('span',class_="pagination")
		new=p[0].contents[-2]['href']
		print new
		url="http://www.imdb.com/"+new
		from_page(url,year)

if __name__ == "__main__":
    for i in [2003,2004,2007,2008,2010]:
    	from_year(i)

