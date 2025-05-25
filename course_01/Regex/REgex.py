from PyPDF2 import PdfReader
import re 

reader = PdfReader("invoice.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
txt = page.extract_text()

print(txt)
# m = re.findall("\$[0-9]*\.[0-9]*",txt)
# print(m)
# m = re.findall("Total Due \$[0-9]*\.[0-9]*",txt)
# print(m)

