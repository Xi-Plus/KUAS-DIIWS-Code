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
for row in rows:
	res = []
	for td in row.findAll(["td", "th"]):
		res.append(td.get_text().strip())
	w.writerow(res)
f.close()
