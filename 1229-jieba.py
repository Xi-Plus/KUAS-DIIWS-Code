import jieba

while True:
	print("/".join(jieba.cut(input())))
