import PyPDF2

with open('AI1.pdf','rb') as p:
    

    data = ""
    r=PyPDF2.PdfFileReader(p)

    print(r.numPages)
    for i in range(r.numPages):
        data = data + r.getPage(i).extractText()

print(data)

