
from pdf2docx import Converter

pdf_file = 'Convert/Convert-PDFToDocx/output1.pdf'
docx_file = 'output.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()