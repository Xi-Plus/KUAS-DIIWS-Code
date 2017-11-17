import urllib.request
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import sys
import os

def ParseUrl(oldurl, newurl, checksame = False):
	oldpares = urlparse(oldurl)
	newpares = urlparse(newurl)
	url = ""
	if newpares.scheme != "":
		url += newpares.scheme
	else :
		url += oldpares.scheme
	url += "://"
	if newpares.netloc != "":
		if checksame and newpares.netloc != oldpares.netloc:
			return ""
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
def checkLink(url):
	try:
		html = urlopen(url).read().decode('utf-8', 'ignore')
		return html
	except Exception as e:
		return ""
def getLinks(url):
	html = checkLink(url)
	if html == "":
		return []
	obj = BeautifulSoup(html, "html.parser")
	links = obj.findAll("a")
	ret = []
	for link in links:
		if link.has_attr("href"):
			ret.append(link["href"])
	return ret

def getImgs(url):
	html = checkLink(url)
	if html == "":
		return []
	obj = BeautifulSoup(html, "html.parser")
	ret = []
	for img in obj.findAll("img"):
		if img.has_attr("src"):
			ret.append(img["src"])
	for img in obj.findAll("input", {"type": "image"}):
		if img.has_attr("src"):
			ret.append(img["src"])
	return ret

if len(sys.argv) > 1:
	url = sys.argv[1]
else :
	url = input("輸入網址：")

if checkLink(url) == "":
	print("網址錯誤或連線錯誤")

Gset = set()
Gsetimg = set()
cnt = 0
def Visit(url, space):
	global cnt
	Gset.add(url)
	links = getLinks(url)
	imgs = getImgs(url)
	for img in imgs:
		img = ParseUrl(url, img, False)
		if img not in Gsetimg:
			cnt += 1
			print("["+str(cnt)+"] "+img)
			Gsetimg.add(img)
	for link in links:
		link = ParseUrl(url, link, True)
		if link != "" and link not in Gset:
			Visit(link, space+"|---")

Visit(url, "")
