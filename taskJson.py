import json
class Base:
    def FileCreate(self,filename):
        with open(filename,"w") as f:
            print(filename + ' '+ "created")
    def FileOpen(self,filename):
        with open(filename,"r+") as f:
            self.data = json.load(f)
            print(self.data)

class DerivedCls1(Base):
    def __init__(self,filename):
        self.filename = filename
        print("i am from child class 1")
        Base.FileOpen(self, self.filename)

    def FileAdd(self,new):
        self.new = new
        with open(self.filename,"r+") as file:
            self.data["ImageAtt"].append(self.new)
            file.seek(0)
            json.dump(self.data,file,indent=4)
            print("data added")

class DerivedCls2(Base):
    def __init__(self,filename):
        self.file = filename
        print("i am from child class 2")
        Base.FileOpen(self,self.file)

obj = DerivedCls1('TaskJsonFile.json')
# obj2 = DerivedCls2('TaskJsonFile.json')
# obj.FileCreate('tasktemp.json')
a = {
      "File name" : "dex",
      "File size" : "8.3kb",
      "Image resolution" : "240x370px",
      "Image name" : "dog3.jpg",
      "No of objects in the image" : 2,
      "Object resolution" : "24x34"
    }
# obj.FileAdd(a)