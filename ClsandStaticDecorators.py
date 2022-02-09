import cowsay
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromDate(cls,name,year):
        return cls(name,date.today().year-year)

    @staticmethod
    def ifAdult(age):
        if age>18:
            cowsay.kitty("I am a kitty  and my name Happy... and my friends call me 'Happy to see you'")
            # return True


s = Person("sam",26)
print("person 1 age is ",s.age)
s2= Person.fromDate("amy",1998)
print("person 2 age is ",s2.age)
print(s.ifAdult(21))
cowsay.ghostbusters("my age is {}".format(s.age))