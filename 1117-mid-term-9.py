from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import csv
import sys
import os

def ParseUrl(oldurl, newurl):
	oldpares = urlparse(oldurl)
	newpares = urlparse(newurl)
	url = ""
	if newpares.scheme != "":
		url += newpares.scheme
	else :
		url += oldpares.scheme
	url += "://"
	if newpares.netloc != "":
		url += newpares.netloc
	else :
		url += oldpares.netloc
	if os.path.dirname(newpares.path) != "":
		url += os.path.dirname(newpares.path)
		if os.path.dirname(newpares.path) != "/":
			url += "/"
	else :
		url += os.path.dirname(oldpares.path)
		if os.path.dirname(oldpares.path) != "/":
			url += "/"
	url += os.path.basename(newpares.path)
	return url

f = open("rfcList.csv", "w", encoding = 'utf8', newline='')
# f.write('\ufeff')
w = csv.writer(f)

if len(sys.argv) > 1:
	url = sys.argv[1]
else :
	url = input("輸入網址：")

try:
	html = urlopen(url).read()
	obj = BeautifulSoup(html, "html.parser")
	for i in obj.findAll("a"):
		w.writerow([ i.get_text(), ParseUrl(url, i["href"]) ])

	f.close()
except Exception as e:
	print("網址錯誤或連線錯誤")
