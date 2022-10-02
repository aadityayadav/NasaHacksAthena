import PyPDF2

def process_pdf(filename):
    fhandle = open(r'apps/static/assets/pdfs/' + filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(fhandle)
    count = pdfReader.numPages
    output = ''
    for i in range(count):
        pagehandle = pdfReader.getPage(i)
        temp = pagehandle.extractText()
        output = output + temp
    return output


# print (output)