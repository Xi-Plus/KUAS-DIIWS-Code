from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

f = open("output.csv", "w", encoding = 'utf8', newline='')
f.write('\ufeff')
w = csv.writer(f)

url = "http://ipv6.twbbs.org/Course/WebScraping/Slide/HTML/ex05_2_csv.html"
html = urlopen(url).read()
obj = BeautifulSoup(html, "html.parser")
rows = obj.findAll("table")[0].findAll("tr")
s = set()
for row in rows:
	res = []
	for td in row.findAll(["td", "th"]):
		res.append(td.get_text().strip())
	if res[0] not in s:
		w.writerow(res)
		s.add(res[0])
f.close()
