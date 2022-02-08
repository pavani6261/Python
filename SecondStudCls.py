# simple inheritance
class Student:   # base class

    # course = "CSE"

    def __init__(self,name,id):  # initialisation
        self.name=name
        self.id=id

    def Details(self):  #function  defination
        age = 21
        print("name - {} id - {} age - {}".format(self.name,self.id,age))

class Address(Student):  #  derived class
    def __init__(self,name, id, adr):
        self.adr = adr
        Student.__init__(self,name,id)  #invoking base class

    def getAdr(self):
        print("address of {} is {}".format(self.name,self.adr))


# A = Student("amy",23)
# B = Student("sam",34)
#
# print("student details are: ")
# A.Details()
# B.Details()

a = Address("amy",23,"hyd")  # creating object to derived class
a.Details()  # using derived class object calling function of base class
a.getAdr()  # calling function in derived class



