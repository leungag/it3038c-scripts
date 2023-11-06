import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r,"lxml")

tags = soup.findAll("a", {"href":re.compile('[<>#%|\{\}!\\^~\[\]`/]')})
for a in tags:
	print(a.get('href'))
