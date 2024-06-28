import PyPDF2

#pdf_in_file = open("simple.pdf",'rb')
pdf_in_file = open("HAPPYBIRTHDAY.pdf",'rb')

inputpdf = PyPDF2.PdfReader(pdf_in_file)
pages_no = len(inputpdf.pages)
output = PyPDF2.PdfWriter()

for i in range(pages_no):
    inputpdf = PyPDF2.PdfReader(pdf_in_file)
    
    output.add_page(inputpdf.pages[i])
    output.encrypt('8765')

    #with open("simple_password_protected.pdf", "wb") as outputStream:
    with open("HAPPY BIRTHDAY.pdf", "wb") as outputStream:
        output.write(outputStream)

pdf_in_file.close()