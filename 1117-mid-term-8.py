from urllib.request import urlopen
import csv
from io import StringIO

url = "http://www.gamerating.org.tw/download_rating.php"

b = urlopen(url).read().decode("utf-8")
f = StringIO(b)
next(f)
r = csv.reader(f, delimiter=',')

res = {}
total = 0
for row in r:
	cats = row[4].split(",")
	for cat in cats:
		if cat not in res:
			res[cat] = 0
		res[cat] += 1
	total += 1

print("Totally "+str(total)+" games")
for cat in res:
	print(cat, res[cat], "("+str(round(100*res[cat]/total, 1))+"%)")
