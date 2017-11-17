from urllib.request import urlopen
from io import BytesIO
import PyPDF2
import csv

f = open("rfcList.csv", "r", encoding = 'utf8')
r = csv.reader(f, delimiter=',')

for row in r:
	b = urlopen(row[1]).read()
	pdfReader = PyPDF2.PdfFileReader( BytesIO(b) )
	for i in range(pdfReader.numPages):
		try:
			s = pdfReader.getPage(i).extractText().lower()
			if "voip" in s:
				print(row[0]+" - "+row[1])
				break
		except Exception as e:
			pass
