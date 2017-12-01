import sys
from urllib.request import urlopen

if len(sys.argv) > 1:
	url = sys.argv[1]
else :
	url = "https://tools.ietf.org/rfc/rfc8200"

text = urlopen(url).read().decode("utf8").upper()
cnt = [0] * 26
for c in text:
	if c >= 'A' and c <= 'Z':
		cnt[ord(c)-ord('A')] += 1

for i in range(26):
	print(chr(i+65), cnt[i])
