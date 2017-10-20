try:
	import sys
	import os.path

	if len(sys.argv) > 1:
		filenames = sys.argv[1:]
	else :
		exit("Useage: python 1020-wc.py filename")

	cntl = 0
	cntw = 0
	cntc = 0
	for filename in filenames:
		if not os.path.exists(filename):
			print("wc: "+filename+": open: No such file or directory")
			continue
		f = open(filename, "r")
		text = f.read()
		f.close()
		l = len(text.split("\n"))-1
		w = len(text.split())
		c = len(text)
		cntl += l
		cntw += w
		cntc += c
		print('%8d%8d%8d %s' % (l, w, c, filename), sep="\t")
	if len(filenames) > 1:
		print('%8d%8d%8d total' % (cntl, cntw, cntc), sep="\t")

except KeyboardInterrupt:
	print("Error")

