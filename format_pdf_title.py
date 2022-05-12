# This is a function that will remove the underscores, reformat the title and remove ".pdf" from the list of PDF names
def FormatPdfTitles(PdfFileList):
    list1 = PdfFileList
    list2 = []

    for x in list1:
        text = x
        text = text.replace("_"," ")
        text = text.replace("-active.pdf"," (Active Only)")
        text = text.replace("-all.pdf"," Guide (All)")
        text = text.replace("ZQ610 ZQ620 QLn220 QLn320","ZQ610/ZQ620/QLn220/QLn320")
        list2.append(text)
    return list2
