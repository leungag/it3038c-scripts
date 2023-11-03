import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.uc.edu/").content
soup = BeautifulSoup(r,"lxml")

tags = soup.findAll("a", {"href":re.compile('[<>#%|\{\}!\\^~\[\]`/]')})
for a in tags:
    href = a.get('href')
    # Check if the href attribute ends with '.html'
    if href.endswith('.html'):
        print(href)


"""
Sample output:
https://www.uc.edu/connect.html
https://admissions.uc.edu/visit.html
https://admissions.uc.edu/apply.html
https://www.uc.edu/scholarships-financial-aid.html
https://www.uc.edu/connect.html
https://admissions.uc.edu/visit.html
https://admissions.uc.edu/apply.html
https://www.uc.edu/scholarships-financial-aid.html
https://www.uc.edu/news/articles/2023/08/n21189138.html

"""