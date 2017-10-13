from urllib.request import urlopen
from urllib.parse import quote
import json

while True:
	address = input("input address: ")
	if address == "":
		break
	url = "http://maps.google.com/maps/api/geocode/json?address="+quote(address)+"&language=zh-TW"
	html = urlopen(url).read()
	data = json.loads(html)
	print(data["results"][0]["formatted_address"])
