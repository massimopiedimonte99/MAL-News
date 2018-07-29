import urllib.request as urllib2

from bs4 import BeautifulSoup


print("\n\t\t--- MAL NEWS ---\n\n\tAuthor: Massimo Piedimonte.\n\tSee my projects on Github: github.com/mynameismaz")

class ScrapeWebsite():

    def __init__(self, url):
        self.url = urllib2.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        self.ok = True

        try:
            self.page = urllib2.urlopen(self.url)
        except:
           self.ok = False


pages = int(input("\n\nNo. pages: "))
page_counter = 0

for i in range(pages):
	print(f"\n\t\t\t\tPage {i + 1}\n", "-"*70, sep="")
	scraper = ScrapeWebsite(f"https://myanimelist.net/news?p={i + 1}")

	if(scraper.ok):
		soup = BeautifulSoup(scraper.page, 'html.parser')
		p = soup.find_all('p', attrs={'class': 'title'})
		for items in p:
			page_counter += 1
			link = items.find('a')
			print(f"{page_counter}) {link.get_text()[0:70]}... - {link['href']}")




print("Done, thanks for using MAL News.\n")
