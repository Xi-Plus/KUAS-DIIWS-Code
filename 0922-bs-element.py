from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://kuas.ipv6.club.tw/~kuas/page1.html"
f = urlopen(url)
html = f.read()
obj = BeautifulSoup(html, "html.parser")
print(obj.prettify())
print(obj.title)
