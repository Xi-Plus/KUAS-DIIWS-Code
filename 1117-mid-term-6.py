from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.books.com.tw/activity/gold66_day/?loc=P_021_1_more_001"
f = urlopen(url)
html = f.read()
obj = BeautifulSoup(html, "html.parser")

days = []
for i in obj.findAll("div", {"class":"day"}):
	days.append(i.get_text())

names = []
for i in obj.findAll("div", {"class":"sec_day"}):
	names.append(i.findAll("a")[1].get_text())

publishs = []
prices = []
prices2 = []
for i in obj.findAll("div", {"class":"sec_day"}):
	temp = i.findAll("h2")
	publishs.append(temp[0].get_text())
	prices.append(temp[1].get_text())
	prices2.append(temp[2].get_text())

for i in range(len(days)):
	print(days[i])
	print(names[i])
	print(prices[i])
	print(prices[i])
	print(prices2[i])
	print()
