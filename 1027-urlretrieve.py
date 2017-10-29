from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import os.path
url = "http://kuas.ipv6.club.tw/~solomon/HTML/ch05_1_urlretrieve.html"
f = urlopen(url)
html = f.read()
obj = BeautifulSoup(html, "html.parser")
imgs = obj.findAll("img")
cnt = 0
for img in imgs:
	cnt += 1
	imgurl = img["src"]
	extension = os.path.splitext(imgurl)[1]
	urlretrieve(imgurl, str(cnt)+extension)
