import jieba
from urllib.request import urlopen

url1 = "http://kuas.ipv6.club.tw/~solomon/HTML/president-20000520.txt"
url2 = "http://kuas.ipv6.club.tw/~solomon/HTML/president-20080520.txt"
url3 = "http://kuas.ipv6.club.tw/~solomon/HTML/president-20160520.txt"

limit = 10

def getmostword(url):
	text = urlopen(url).read().decode("utf8")
	dic = {}
	for token in jieba.cut(text):
		if token not in dic:
			dic[token] = 0
		dic[token] += 1

	dic = sorted(dic.items(), key=lambda v:v[1], reverse=True)
	cnt = 0;
	result = []
	for v in dic:
		if len(v[0]) < 2:
			continue
		cnt += 1
		result.append([v[0], v[1]])
		if cnt == limit:
			break
	return result

result1 = getmostword(url1)
result2 = getmostword(url2)
result3 = getmostword(url3)

print("{:12}      {:12}      {:12}".format("陳水扁", "馬英九", "蔡英文"))
print("{:15}      {:15}      {:15}".format("="*15, "="*15, "="*15))
for i in range(limit):
	print("{:15}    {:15}    {:15}".format(
		"('{}', {})".format(result1[i][0], result1[i][1]),
		"('{}', {})".format(result2[i][0], result2[i][1]),
		"('{}', {})".format(result3[i][0], result3[i][1])))
