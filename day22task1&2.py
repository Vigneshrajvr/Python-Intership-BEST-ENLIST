from PIL import Image
import PyPDF2
im1 = Image.open(r"doggy.jpg")
print("Copied Image.....")
print("Showing image.....")
im2 = im1.copy()
im2.show()
 
def PDFmerge(pdfs, output):
    pdfMerger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        pdfMerger.append(pdf)
    with open(output, 'wb') as f:
        pdfMerger.write(f)
        
pdfs = ['PDF.pdf', 'PDF2.pdf']
output = 'combined_pdf.pdf'
print("Reading the PDF.....")
PDFmerge(pdfs=pdfs, output=output)
print("PDF merged succesful")
