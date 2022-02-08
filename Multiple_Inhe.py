## Multiple inheritance
class Student:
    name = "Joe"
    Id = 123
    def StudDetails(self):
        print(f"name: {self.name}, id : {self.Id}")

class Department(Student):
    dep = "CSE"
    def DepDetails(self):
        print(f"department : {self.dep}")

class Admin(Department):
    def Display(self):
        print("detail are:")

A = Admin()
A.DepDetails()
A.StudDetails()
