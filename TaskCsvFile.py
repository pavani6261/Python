import csv
class Base:
    def FileOpen(self,file):  # create file
        self.file = file
        with open(self.file,"w") as f:
            print("created file at ",self.file)
    def FileWrite(self,filename): # writing in dictionary form
        self.file = filename
        HeaderList = ["File name", "File size", "Image resolution", "Image name", "No of objects in the image", "Object resolution"]

        with open(self.file, "r+", newline='') as f1:
            w1 = csv.DictWriter(f1, fieldnames= HeaderList)
            w1.writeheader()
            w1.writerow({"File name":"abc", "File size":"7kb", "Image resolution":"240x370px", "Image name":"rose.jpg", "No of objects in the image":3, "Object resolution":"24x34"})
            w1.writerow({"File name":"abc2", "File size":"6.7kb", "Image resolution":"240x370px", "Image name":"dog.jpg", "No of objects in the image":4, "Object resolution":"24x34"})
            w1.writerow({"File name":"abc3", "File size":"8.2kb", "Image resolution":"240x370px", "Image name":"flower.jpg", "No of objects in the image":2, "Object resolution":"24x34"})

class Derived(Base):
    def FileRead(self,file):  #reading and displaying row by row
        self.file = file
        with open(self.file,"r",newline= '') as f:
            data = csv.reader(f, delimiter=' ')
            for row in data:
                print(' '.join(row))
    def FileDictRead(self,filename): #reading the file and displaying in dict format
        self.file = filename
        with open(self.file,"r",newline= '') as f:
            data = csv.DictReader(f)
            for row in data:
                print(dict(row))
a = Derived()
# a.FileOpen('C:\CsvFiles\TaskCsv2.csv')
# a.FileWrite('C:\CsvFiles\TaskCsv2.csv')
# a.FileRead('C:\CsvFiles\TaskCsv2.csv')
a.FileDictRead('C:\CsvFiles\TaskCsv2.csv')