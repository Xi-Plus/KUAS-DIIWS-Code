import jieba
from urllib.request import urlopen

url1 = "http://kuas.ipv6.club.tw/~solomon/HTML/login.20171117.txt"
url2 = "http://solomon.ipv6.club.tw/Course/WebScraping/kuas-student.txt"
text1 = urlopen(url1).read().decode("utf8")
text2 = urlopen(url2).read().decode("utf8")

students = {}
for line in text2.split("\n"):
	line = line.split()
	if len(line) != 2:
		continue
	students[line[0]] = line[1]

for line in text1.split("\n"):
	uid = line[:10]
	if uid in students:
		del students[uid]

for uid in students:
	print(uid, students[uid])