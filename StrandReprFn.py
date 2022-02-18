# import datetime
# name = "Hello"
# a = ["er",23,"eret"]
#
# print(a)  # str fn - creating output for end user
# print([a])  #represent function - repr() or [] --- debugging and development
#
# b = datetime.datetime.now()
# print(str(b))
# print(repr(b))  #official or in-built format

class Learn:
    def __init__(self,a,b):
        self.a= a
        self.b = b
    def __repr__(self):
        return "from repr method a: %s b: %s" %(self.a,self.b)
    def __str__(self):
        return "from str method a: %s," "b: %s" % (self.a,self.b)

l = Learn(23,45)
print(l) # calls str()
print([l]) # calls repr()