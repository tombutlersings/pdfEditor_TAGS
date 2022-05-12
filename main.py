# Finished May 12, 2022
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pprint
from PyPDF2 import PdfFileReader, PdfFileMerger
from file_evaluator import ActiveOrAll
from Pdf import Pdf
from meta_title_creator import meta_title_creator
from pdf_list_of_files import pdf_list_of_files

PDF_FOLDER = "C:/Users/tb3655/OneDrive - Zebra Technologies/TAG Files/Production Version/Meta_Data_Program/unfinished/*.pdf"
UNFINISHED_FOLDER = "C:/Users/tb3655/OneDrive - Zebra Technologies/TAG Files/Production Version/Meta_Data_Program/unfinished/"
FINISHED_FOLDER = "C:/Users/tb3655/OneDrive - Zebra Technologies/TAG Files/Production Version/Meta_Data_Program/finished/"
pdf_list_of_names = []


### TODO: STEP 1: list PDF's in folder and verify you'd like to proceed with conversion

def main():
    pdf_list_of_names = pdf_list_of_files(PDF_FOLDER)
    list_len = len(pdf_list_of_names)
    pdf_num = 0
    while pdf_num < list_len:
        p1 = Pdf()
        p1.setFileName(pdf_list_of_names[pdf_num])
        p1.setFileLoc(UNFINISHED_FOLDER, p1.filename)
        p1.meta_title = meta_title_creator(p1.filename)

        # in this part we will also define our font color and the font size:
        # FROM: https://dev.to/stokry/edit-pdf-files-with-python-1e1j
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
        # Working opener and editor of metadata
        # from https://stackoverflow.com/questions/46849733/change-metadata-of-pdf-file-with-pypdf2?newreg=d1ea14de43084962a613403ee674d419

        file_in = open(p1.file_location, "rb")
        pdf_reader = PdfFileReader(file_in)
        metadata = pdf_reader.getDocumentInfo()
        pprint.pprint(metadata)

        pdf_merger = PdfFileMerger()
        pdf_merger.append(file_in)
        p1.setAuthor("Tom Butler")
        p1.setKeywords()
        pdf_merger.addMetadata({
            '/Author': p1.author,
            '/Title': p1.meta_title,  # fixed 5-11-2022 make this dynamic
            '/Keywords': p1.meta_keywords  # fill up the keywords
        })

        # THIS IS THE FILE WHERE THE META DATA IS ADDED
        # fixed 5-11-22: title still hardcoded, fix that
        file_out = open(p1.file_location_out, 'wb')
        pdf_merger.write(file_out)

        file_in.close()
        file_out.close()
        pdf_num += 1


if __name__ == "__main__":
    main()
