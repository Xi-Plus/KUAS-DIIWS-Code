import sys

maxlength = 100

arr = [[0 for i in range(maxlength)] for j in range(maxlength)]
if len(sys.argv) > 1:
	file = sys.argv[1]
	f = open(file, "r")
	for row in f:
		row = row.split()
		if len(row) == 0:
			break
		if len(row) >= 2:
			arr[int(row[0])][int(row[1])] = 1
			print(int(row[0]), int(row[1]))
	row = f.read()
	row = row.split()
	s = int(row[0])
	t = int(row[1])
	print()
	print(s, t)
else :
	while True:
		text = input()
		if text == "":
			break
		text = text.split()
		if len(text) >= 2:
			arr[int(text[0])][int(text[1])] = 1
	text = input()
	text = text.split()
	s = int(text[0])
	t = int(text[1])

fromp = [-1 for i in range(maxlength)]
pathlen = [999999 for i in range(maxlength)]

pathlen[s] = 0

def dfs(p, f, d):
	if d < pathlen[p]:
		fromp[p] = f
		pathlen[p] = d
	for i in range(maxlength):
		if arr[p][i]:
			arr[p][i] = 0
			dfs(i, p, d+1)

dfs(s, s, 0)

path = []
def getpath(p):
	path.append(p)
	if p == -1:
		return
	if p == s:
		return
	getpath(fromp[p])

getpath(t)

if path[-1] == -1:
	print("cannot find path")
else :
	path.reverse()
	print(path)
