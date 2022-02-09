# encapsulation : using access specifiers : public, private and protected variables
class College:
    clgname = "Vaagdevi"    #public variable :can be access in whole program using instance
    # clgname is also  static variable
    def Display(self,code):
        self._clgCode= code  #protected variable  : can be accessed by class and derived class
        print(f"college name is {self.clgname}")
        print("college code is {}".format(self._clgCode))

class Student(College):
    def __init__(self,name,id):
        self.name = name # also known as instance variable
        self.__id = id   #private variable :used only in this class and by using "name mangling" we can access outside the class
    def Details(self):
        print("student name is {} and id is {}".format(self.name,self.__id) )
        # print("college name  and code are {} - {} ".format(self.clgname,self._clgCode))

a = Student("sam",123)
a.Details()
# print(a.name) # public variable
# print(a.__id)  # private variable can not be access
print(a._Student__id) #using name mangling : _className__variableName
a.Display("v1") # using the instance object of derived class calling the base cls fn
print(a.clgname)
# a.clgname = "SR"
# print(f"changed clg name using instance obj of derived cls is {a.clgname}")
# print(f"static variable value after changing through instance is :{College.clgname}")
# College.clgname = "SVR"
# print(f"static variable value after changing through base class name is :{College.clgname}")
# print(f"after changing clg name using base cls the instance clgname variable value is {a.clgname}")
# b = College()
# b.Display("S21")