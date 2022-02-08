## multi - level inheritance
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def Display(self):
        print(f"name: {self.name}, id : {self.id}")

class Department(Student):
    def __init__(self,name,id,dep):
        self.dep = dep
        Student.__init__(self,name,id)
        # Student.Display(self)
        print(f"department : {self.dep}")

class Admin(Department):
    def Details(self):
        print("detail are:")

a = Admin("John",23,"CSE") # creating object for class Admin
b = Department("amy",24,"ECE") # creating object for class Department
a.Details()  # calling the function in Admin class
a.Display()  # calling the function of super class using object of Admin class
b.Display()  # using Department object calling function of Student class