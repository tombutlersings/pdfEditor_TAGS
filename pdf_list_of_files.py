import glob


def pdf_list_of_files(PDF_FOLDER):
    char_len = len(PDF_FOLDER) - 5
    # https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    file_list = glob.glob(PDF_FOLDER)
    file_len = len(file_list) + 1
    j = 1
    pdf_list_of_names = []
    # pdf file name format stripper
    print("The files in this folder are: ")
    j = 1
    for x in file_list:
        text = str(x)
        text = text[char_len:]
        print(str(j) + ". " + text)
        j += 1
        pdf_list_of_names.append(text)
    return pdf_list_of_names
