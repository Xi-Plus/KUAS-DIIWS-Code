from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.mis.kuas.edu.tw/main.php?mod=teacher&site_id=0"
f = urlopen(url)
html = f.read()
obj = BeautifulSoup(html, "html.parser")
names = obj.findAll("font", {"color":"blue"})
emails = obj.select('a[href^=mailto:]')
cnt = 0
for name in names:
	print(name.get_text()+" "+emails[cnt].get_text())
	cnt += 1
