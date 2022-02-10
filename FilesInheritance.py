import json
class Base:
    def FileOpen(self,filename):
        with open(filename,"r+") as f:
            self.data = json.load(f)
            print(self.data)

class DerivedCls1(Base):
    def __init__(self,filename):
        self.filename = filename
        Base.FileOpen(self, self.filename)
    def FileWrite(self,new2):
        self.new_data = {
            "name": "Davin",
            "id": "20",
            "age": "34"
        }
        self.new2 = new2
        with open(self.filename,"r+") as file:
            self.data["employee"].append(self.new2)
            file.seek(0)
            json.dump(self.data,file,indent=4)

c = DerivedCls1('JsonDataFile1.json')
a= {
    "name" : "Hema",
    "id" : "19",
    "age" : "35"
}
c.FileWrite(a)
c.FileOpen('JsonDataFile1.json')