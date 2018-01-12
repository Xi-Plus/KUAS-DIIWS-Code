from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
f = urlopen(url)
html = f.read()
obj = BeautifulSoup(html, "html.parser")
table = obj.findAll("table")[0]
trs = table.findAll("tr")
dic = {}
arr = []
for tr in trs:
	tds = tr.findAll("td")
	cnt = 0
	tmp = []
	for td in tds:
		if cnt == 0:
			tmp.append(td.findAll("div", {"class":"hidden-phone print_show"})[0].get_text().strip())
		else :
			tmp.append(td.get_text().strip())
		cnt += 1
	if len(tmp) == 0:
		continue

	m = re.match(r"(.+) \((.+?)\)", tmp[0])
	zhname = m.group(1)
	enname = m.group(2)
	v1 = tmp[1]
	v2 = tmp[2]
	if v1 == "-":
		v1 = 0.0
	if v2 == "-":
		v2 = 0.0
	dic[enname] = {"zhname":zhname, "v1":v1, "v2":v2}
	arr.append(enname)

for i in range(len(arr)):
	print(str(i+1)+". "+dic[arr[i]]["zhname"]+" ("+arr[i]+")")

while True:
	instr = input("Please choose the number corresponding to the currency you want to know, or the currency code (USD, EUR, JPY, ...): ")
	if instr == "":
		break
	try:
		i = int(instr)
		enname = arr[i-1]
	except ValueError as e:
		instr = instr.upper().strip()
		if instr in dic:
			enname = instr
		else :
			print("Wrong index or Wrong code, Please input again!")
			continue
	except IndexError as e:
		print("Wrong index or Wrong code, Please input again!")
		continue
	
	if i == 0:
		break
	
	print(dic[enname]["zhname"]+" ("+enname+") "+str(dic[enname]["v1"])+"買入 "+str(dic[enname]["v2"])+"賣出")
