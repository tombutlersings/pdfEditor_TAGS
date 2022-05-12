# pull the file name and make it a text variable
# parse the file to find out whether it is the active only or all
import fitz  # this is pymupdf


# TODO: create a def for the new PDF filename (versus the above which is the titlename OR MAYBE just add a attribute for title or filename
def ActiveOrAll(unfin_file_location, pdf):
    f = unfin_file_location
    with fitz.open(f) as doc:
        text = ''
        # other_text = ''
        for page in doc:
            text += page.get_text()
            # other_text += page.extractTEXT()
    x = text.find("Version: Active Only")
    # -1 means it was not found
    print(x)
    if x != -1:
        pdf.setActive()
    else:
        pdf.disableActive()