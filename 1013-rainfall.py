from urllib.request import urlopen
import json

html = urlopen("http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$format=json").read()
datas = json.loads(html)
requestCounty = ["宜蘭縣", "高雄市"]
print("Site\tCounty\tPublishTime\t10min\t24hr")
for data in datas:
	if data["County"] in requestCounty:
		print(data["SiteName"]+"\t"+data["Township"]+"\t"+data["PublishTime"]+"\t"+data["Rainfall10min"]+"\t"+data["Rainfall24hr"])
