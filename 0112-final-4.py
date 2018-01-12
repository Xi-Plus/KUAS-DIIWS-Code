from urllib.request import urlopen
from io import StringIO
import csv

url = "http://stats.moe.gov.tw/files/detail/105/105_student.csv"
b = urlopen(url).read().decode("utf-8")
f = StringIO(b)
next(f)
r = csv.reader(f, delimiter=',')

dic = {}

for line in r:
	total = 0
	name = line[1]
	for i in range(4, 20):
		total += int(line[i])
	if name not in dic:
		dic[name] = 0
	dic[name] += total
dic = sorted(dic.items(), key=lambda v:v[1], reverse=True)

for i in range(len(dic)):
	print("[%3d] %s %d" % (i+1, dic[i][0], dic[i][1]))
