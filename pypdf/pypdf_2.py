from pyPdf import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
input1 = PdfFileReader(file("document1.pdf", "rb"))
watermark = PdfFileReader(file("watermark.pdf", "rb"))

input1.mergePage(watermark.getPage(0))

# finally, write "output" to document-output.pdf
outputStream = file("document-output.pdf", "wb")
output.write(input1)
outputStream.close()
