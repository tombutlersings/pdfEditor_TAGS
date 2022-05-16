import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def blankPdfMaker(pdf,file_location):
    p1 = pdf
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFillColorRGB(1, 0, 0)
    can.setFont("Times-Roman", 14)
    can.drawString(72, 655, "Hello from Python")
    can.save()
    # Then we move to the beginning of the StringIO buffer:
    packet.seek(0)
    unedited_pdf_name = p1.file_location
    unedited_pdf_name.replace("_", " ")  # Swaps '_' for space
    unedited_pdf_name.replace(".pdf", " ")  # Swaps '_' for space
    existing_pdf = PdfFileReader(open(unedited_pdf_name, "rb"))
    output = PdfFileWriter()

    # figures out number of pages in the original PDF
    pdf_pages = existing_pdf.numPages

    # uses the page numbers to make sure all of them get added back to the new pdf
    i = 0
    while i < pdf_pages:
        page = existing_pdf.getPage(i)
        output.addPage(page)
        i += 1
    outputStream = open(p1.file_location_out, "wb")
    output.write(outputStream)
    outputStream.close()
