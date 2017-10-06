try:
	import urllib.request
	from urllib.request import urlopen
	from urllib.parse import urlparse
	from bs4 import BeautifulSoup
	import sys
	import os

	print(os.path.dirname("/~solomon/HTML/c5.html"))
	if len(sys.argv) > 1:
		url = sys.argv[1]
	else :
		url = input("Please input a url: ")

	def ParseUrl(oldurl, newurl):
		oldpares = urlparse(oldurl)
		newpares = urlparse(newurl)
		# print(oldpares)
		# print(newpares)
		url = ""
		if newpares.scheme != "":
			url += newpares.scheme
		else :
			url += oldpares.scheme
		url += "://"
		if newpares.netloc != "":
			url += newpares.netloc
		else :
			url += oldpares.netloc
		# print("a "+url)
		if os.path.dirname(newpares.path) != "":
			url += os.path.dirname(newpares.path)
			# print("c "+newpares.path)
			# print("c "+os.path.dirname(newpares.path))
		else :
			url += os.path.dirname(oldpares.path)
			# print("d "+oldpares.path)
			# print("d "+os.path.dirname(oldpares.path))
		# print("b "+url)
		url += "/"
		url += os.path.basename(newpares.path)
		return url
	def getLinks(url):
		try:
			html = urlopen(url).read()
			obj = BeautifulSoup(html, "html.parser")
			links = obj.findAll("a")
			ret = []
			for link in links: 
				# print(link.attrs("href"))
				# if "href" in link.attrs("href"):
				# print(link["href"])
				ret.append(link["href"])
			return ret
		except ValueError:
			print("輸入的不是一個網址，必須http或https開頭:"+url)
		except TimeoutError:
			print("連線逾時:"+url)
		except urllib.error.URLError as e:
			print("連線錯誤，原因:"+str(e.reason)+":"+url)
		except ConnectionAbortedError:
			print("網路變更:"+url)
		return []

	# print(url)
	# while True:
	# 	print(ParseUrl(url, input()))

	# links = getLinks(url)
	# for link in links:
		# print(link)
		
		# print()
	Gset = set()
	def Visit(url, space):
		Gset.add(url)
		print(space+url)
		links = getLinks(url)
		for link in links:
			link = ParseUrl(url, link)
			if link not in Gset:
				Visit(link, space+"|---")
	Visit(url, "")
	print("end")
		

except KeyboardInterrupt:
	print("取消操作")
