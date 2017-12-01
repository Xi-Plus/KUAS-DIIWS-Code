import sys
import re
from urllib.request import urlopen

if len(sys.argv) > 1:
	url = sys.argv[1]
else :
	url = input("input a url: ")

text = urlopen(url).read().decode("utf8").lower()
text = re.sub("[^a-z0-9]", " ", text)
text = re.sub(" +", " ", text)
text = text.split()

cnt = {}
for word in text:
	if len(word) > 1:
		if word not in cnt:
			cnt[word] = 0
		cnt[word] += 1
cnt = sorted(cnt.items(), key=lambda v:v[1])
for v in cnt:
	print(v[0], v[1])
# print(cnt)
