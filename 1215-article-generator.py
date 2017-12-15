import urllib.request
import re
import random
import json

urls = [
		"http://kuas.ipv6.club.tw/~1105108134/1215/test.txt",
		"http://kuas.ipv6.club.tw/~solomon/HTML/ch08_mergeNews_01.txt",
		"http://kuas.ipv6.club.tw/~solomon/HTML/ch08_mergeNews_02.txt",
		"http://kuas.ipv6.club.tw/~solomon/HTML/ch08_mergeNews_03.txt",
		"http://kuas.ipv6.club.tw/~solomon/HTML/ch08_mergeNews_04.txt",
	]
text = ""
for url in urls:
	text += urllib.request.urlopen(url).read().decode("utf8")
text = re.sub("\n+", "", text)
text = re.sub(" +", "", text)

dic = {}
for i in range(len(text)-1):
	if text[i] not in dic:
		dic[text[i]] = {"len": 0, "list": {}}
	if text[i+1] not in dic[text[i]]["list"]:
		dic[text[i]]["list"][text[i+1]] = 0
	dic[text[i]]["list"][text[i+1]] += 1
	dic[text[i]]["len"] += 1

start = list(dic.keys())[random.randint(0, len(dic.keys()))]
print(start, end="")
for _ in range(1000):
	i = random.randint(1, dic[start]["len"])
	for char in dic[start]["list"]:
		new = char
		i -= dic[start]["list"][char]
		if i <= 0:
			break
	print(new, end="")
	start = new
print()
