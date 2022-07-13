# importing required modules
import PyPDF2
def read_pdf(file_name):
    pdfFileObj = open(file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    text = (pageObj.extractText())
    print(text)

