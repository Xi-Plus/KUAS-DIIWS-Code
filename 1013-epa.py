from urllib.request import urlopen
import json

html = urlopen("https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000259").read()
datas = json.loads(html)
requestCounty = ["南投縣", "高雄市"]
print("SiteName", "PublishTime", "PM2.5", "AQI", "Status", "WindSpeed")
for data in datas["result"]["records"]:
	if data["County"] in requestCounty:
		print(data["SiteName"], data["PublishTime"], data["PM2.5"], data["AQI"], data["Status"], data["WindSpeed"])
