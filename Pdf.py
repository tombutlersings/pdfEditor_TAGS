class Pdf:

    def __init__(self):
        self.filename = "Unchanged.pdf"
        self.file_location = ""
        self.meta_title = "unchanged title"
        self.author = "unchanged metadata author"
        self.meta_keywords = "unchanged metadata keywords"
        self.active = False
        self.file_location_out = ""

    def getFilename(self):
        x = self.filename
        return x

    def setFileName(self, filename):
        # print("received " + str(filename) + " from main.py")
        self.filename = filename

    def printFilename(self):
        x = self.filename
        print(x)

    def getFileLoc(self):
        x = self.file_location
        return x

    def setFileLoc(self,folder,filename):
        x = folder + filename
        self.file_location = x
        y = x.replace("unfinished","finished")
        self.file_location_out = y

    def printFileLoc(self):
        print(self.file_location)

    def printKeywords(self):
        print(self.meta_keywords)

    def setKeywords(self):
        x = self.filename
        y = x[:2]
        if y == "ZQ" or y == "QL":
            z = str(x[:5])
            self.meta_keywords = z + "," + "Zebra,Industrial,Mobile,Printer,Healthcare,Warehouse,Distribution,Manufacturing,Picker,Courier,Delivery,Hands-free"
        elif y == "ZD" or y == "GX":
            z = str(x[:5])
            self.meta_keywords = z + "," + "Zebra,Industrial,Desktop,Printer,Healthcare,Warehouse,Distribution,Manufacturing,Retail,Government,Office"
        elif y == "ZT":
            z = str(x[:5])
            self.meta_keywords = z + "," + "Zebra,Industrial,Tabletop,Transportation,Automotive,24/7,Printer,Healthcare,Warehouse,Distribution,Manufacturing"

    def setAuthor(self,author):
        self.author = author

    def printTitle(self):
        print(self.meta_title)

    def printAuthor(self):
        print(self.author)

    def setActive(self):
        self.active = True

    def disableActive(self):
        self.active = False

    def getActive(self):
        return self.active

    def printType(self):
        x = str(self.active)
        print(x)
