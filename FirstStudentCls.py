class Student:    # creating class Student

    course = "CSE"  ## global variable

    def __init__(self,name,id):
        self.name=name
        self.id=id

    def Details(self):   # function defination
        age = 21   # local variable
        print("name - {} id - {} age - {}".format(self.name,self.id,age))


A = Student("amy",23)   #creating object to student class with values
B = Student("sam",34)

print("student details are: ")
A.Details()  # function call
B.Details()

print("course of student name- {} is {}".format(A.name,A.__class__.course))  # accessing global variable
print("course of student name- {} is {}".format(B.name,B.__class__.course))