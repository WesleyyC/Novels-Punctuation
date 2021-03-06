from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from txt2pdf import pyText2Pdf
import re
import sys

pdf = False

def convert_pdf_to_txt(path):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
	fp = file(path, 'rb')
	interpreter = PDFPageInterpreter(rsrcmgr, device)
	password = ""
	maxpages = 0
	caching = True
	pagenos=set()

	for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
		interpreter.process_page(page)

	text = retstr.getvalue()

	fp.close()
	device.close()
	retstr.close()
	return text

def filter_text(txt):
	p = re.compile('\w')
	return p.sub(' ', txt)

def write_to_txt(txt,output_path):
	f = open(output_path+'.txt', 'w')
	f.write(txt)
	f.close()

def write_to_pdf(output_path):
	pdfFile = pyText2Pdf()
	pdfFile.SetIO(output_path+'.txt',output_path+'.pdf')
	pdfFile.Convert()

if __name__ == "__main__":
	path = sys.argv[1]

	output_path = path[:path.rfind('.')]+"_output"

	txt = convert_pdf_to_txt(path)
	txt = filter_text(txt)

	write_to_txt(txt,output_path)

	if pdf:
		write_to_pdf(output_path)
