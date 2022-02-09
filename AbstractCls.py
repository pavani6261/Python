## Abstaction
import abc #importing abstract class

class Sample(abc.ABC): # ABC is helper class
    @abc.abstractmethod  # decorator
    def Display(self):
        pass
    def Add(self):
        pass

class Sample2(Sample):
    def Display(self,a,b):
        print(a,b)

    def Add(self,a,b):
        return a+b

class Sample3(Sample):
    def Add(self,a,b,c):
        return a+b+c
    def Display(self):
        print("Hello")
x = Sample2()
x.Display(2,3)
print(x.Add(4,6))
y = Sample3()
print(y.Add(1,2,3))
y.Display()
