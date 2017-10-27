from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
url = "http://kuas.ipv6.club.tw/~solomon/HTML/ch05_1_urlretrieve.html"
f = urlopen(url)
html = f.read()
obj = BeautifulSoup(html, "html.parser")
imgs = obj.findAll("img")
cnt = 0
for img in imgs:
	print(img["src"])
	cnt += 1
