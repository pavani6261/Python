
import xmltodict
import pprint
class Xml:
    def FileOpen(self,filename):
        with open(filename,"w") as f:
            print(filename + ' '+ "created")
    def FileRead(self,filename):
        with open(filename,"r+") as f:
            self.data = f.read()
            # print(self.data)

class PyDict(Xml):
    def __init__(self,filename):
        self.fn = filename
        super(PyDict,self).FileRead(self.fn)

    def Output(self):
        Dict = xmltodict.parse(self.data)
        pprint.pprint(Dict)

a = PyDict('XmlFile.xml')
a.Output()