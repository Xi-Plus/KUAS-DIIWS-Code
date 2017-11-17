from urllib.request import urlopen
import PyPDF2
from io import BytesIO
b = urlopen("http://zempirians.com/ebooks/Ryan%20Mitchell-Web%20Scraping%20with%20Python_%20Collecting%20Data%20from%20the%20Modern%20Web-O'Reilly%20Media%20(2015).pdf").read()
pdfReader = PyPDF2.PdfFileReader( BytesIO(b) )
cnt = 0
for i in range(pdfReader.numPages):
	s = pdfReader.getPage(i).extractText()
	if "SQL" in s:
		f = s.find("SQL")
		print("==="+str(i)+"===")
		print(s[f-50:f+50])
		cnt += 1

print(cnt)
