import jieba
from urllib.request import urlopen

url = "http://kuas.ipv6.club.tw/~solomon/HTML/sanguo-001.txt"
text = urlopen(url).read().decode("utf8")

jieba.load_userdict("userdict.txt")

tokens = jieba.cut(text)
print("/".join(tokens))

dic = {}
for token in tokens:
	if token not in dic:
		dic[token] = 0
	dic[token] += 1

dic = sorted(dic.items(), key=lambda v:v[1], reverse=True)
cnt = 0;
for v in dic:
	cnt += 1
	print(cnt, v[0], v[1])
	if cnt == 100:
		break
