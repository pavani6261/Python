#if base class and derived class has same function name then to specify the base class function we use super keyword
## metod overriding using super keyword
class College:
    clgname =  "VAGE"
    def __init__(self,name):
        self.name = name

    def Display(self):
        print(f"name of student is {self.name}")
    print(f"name of college is {clgname}")
class Student(College):

    def __init__(self,name,id):
        # self.sname = name
        self.id = id
        super(Student,self).__init__(name)
        super(Student,self).Display()

    def Display(self):
        print(f"name and id of student is {self.name,self.id} ")

a = Student("Joe",23) #instance of derived class
a.Display()  # calling the derived class function
print(a.clgname)
b = College("amy")  #creating object to base class
b.Display()  #calling base class function with instance of base class
