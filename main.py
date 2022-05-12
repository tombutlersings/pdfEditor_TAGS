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
        p1.setFileLoc(UNFINISHED_FOLDER,p1.filename)
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
            total_pages = str(pdf_pages)
            # print("adding page ")
            # print(i+1)
            # print("of " + total_pages)
            page = existing_pdf.getPage(i)
            output.addPage(page)
            i += 1
        # Then we add the "watermark" (which is the new pdf) on the existing page;
        # page = existing_pdf.getPage(0)
        # page.mergePage(new_pdf.getPage(0))
        # output.addPage(page)
        # And finally, write "output" to a real file:
        #current location of the file
        # evaluate the file to see if its active only or not
        # UNECESSARY ofname = "C:/Users/tb3655/OneDrive - Zebra Technologies/TAG Files/Production Version/Meta_Data_Program/finished/destination.pdf"
        outputStream = open(p1.file_location_out, "wb")
        output.write(outputStream)
        outputStream.close()
        # TODO: FIGURE OUT IF DOC IS ACTIVE ONLY OR NOT
        is_active = ActiveOrAll(p1.file_location,p1)
        # print("the pdf is Active Only: " + str(is_active))

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
            '/Keywords': p1.meta_keywords #fill up the keywords
        })

        # THIS IS THE FILE WHERE THE META DATA IS ADDED
        # fixed 5-11-22: title still hardcoded, fix that
        file_out = open(p1.file_location_out, 'wb')
        pdf_merger.write(file_out)

        file_in.close()
        file_out.close()
        pdf_num += 1
    # STEP 1: list PDF's in folder and verify you'd like to proceed with conversion
    # STEP 2: validate PDF type (all or active)
    # STEP 3: autogenerate new blank pdf file
    # STEP 4: export old pdf to new pdf (basically exporting same pdf to new destination PDF)
    # STEP 5: autogenerate and add new meta-data title
    # STEP 6: autogenerate and add new meta-data Author
    # STEP 7: autogenerate and add new meta-data keywords
    # STEP 8: validate new files with -all contain "Version: All"
    # STEP 9: validate new files with -active contain "Version: Active Only"
    # STEP 10: print completion log of everything done and updated to a log file in the destination folder titled with timestamp
    #     and containing every file that was updated during this procedure


    # from PyPDF2 import PdfFileReader
    # pdf_toread = PdfFileReader(open("ZD420D_Technical_Accessory_Guide_All.pdf", "rb"))
    #
    # pdf_info = pdf_toread.getDocumentInfo()
    # print(str(pdf_info))

    # TODO: This is my original code that kind of worked
    # from pdfminer.pdfparser import PDFParser
    # from pdfminer.pdfdocument import PDFDocument
    #
    # fp = open('ZD420D_Technical_Accessory_Guide_All.pdf', 'rb')
    # parser = PDFParser(fp)
    # doc = PDFDocument(parser)
    #
    # print(doc.info)  # The "Info" metadata
    # auth = str(doc.info[0].get("Author"))
    # auth_orig = doc.info[0].get("Author")
    # title = str(doc.info[0].get("Title"))
    # title_orig = doc.info[0].get("Title")
    # print("The pdf Title is: " + title)
    # print("The pdf Author is: " + auth)
    # auth2 = {'Author':b'Tom Butler'}
    # TODO: This is the END of my original code that kind of worked


    # TODO: OLD CODE FOR PARSING - begin
    # find out type of document it is
    # from: https://stackoverflow.com/questions/17098675/searching-text-in-a-pdf-using-python


    # # open the pdf file
    # object = PyPDF2.PdfFileReader("destination.pdf")
    #
    # # get number of pages
    # NumPages = object.getNumPages()
    #
    # # define keyterms
    # String = "Version: Active Only"
    #
    # # extract text and do the search
    # for i in range(0, NumPages):
    #     PageObj = object.getPage(i)
    #     print("this is page " + str(i))
    #     Text = PageObj.extractText()
    #     print(Text)
    #     ResSearch = re.search(String, Text)
    #     print(ResSearch)
    # TODO: OLD CODE FOR PARSING - end



if __name__ == "__main__":
    main()
