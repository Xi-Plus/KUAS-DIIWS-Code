import jieba
from urllib.request import urlopen

url = "http://course.ipv6.club.tw/WebScraping/rfcReference.txt"
text = urlopen(url).read().decode("utf8")

dic = {}
fromid = {}
fromlen = {}
cidlist = []
for line in text.split("\n"):
	line = line.replace(":", "").split()
	if len(line) == 0:
		continue

	cid = int(line[0])

	fromid[cid] = -1
	fromlen[cid] = 99999999
	cidlist.append(cid)
	
	dic[cid] = []
	for i in range(1, len(line)):
		dic[cid].append(int(line[i]))

cidlist.reverse()

while True:
	try:
		start = int(input("start id: "))
		if start not in fromid:
			print(str(start)+" not exist!")
			continue
		break
	except ValueError as e:
		print("please input number")

while True:
	try:
		end = int(input("end id: "))
		if end not in fromid:
			print(str(end)+" not exist!")
			continue
		break
	except ValueError as e:
		print("please input number")

queue = [[start, start]]
while len(queue):
	now = queue.pop(0)
	cid = now[0]
	if fromid[cid] == -1:
		fromid[cid] = now[1]
	for i in dic[cid]:
		if i in fromid and fromid[i] == -1:
			queue.append([i, cid])

if fromid[end] == -1:
	print("path not found\n")
else :
	now = end
	path = []
	while now != start:
		path.append(str(now))
		now = fromid[now]
	path.append(str(start))
	path.reverse()
	print("path is: "+", ".join(path))
