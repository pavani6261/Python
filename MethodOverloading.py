## method overloading : using default arguments

# def Sum(a,b,c=0):  #3rd arg is declared as default c=0
#     return a+b+c
#
# print(Sum(3,8,4)) ## a=3,b=8, c=4
# print(Sum(3,5))  ##sum() declared 3 arg but we are passing only 2 arg. so it takes the default value 0 for c variable

## using variable length argument

def Display(*a):
    for i in range(len(a)):
        return a

print(Display(2,3,4))
print(Display(1,2,3,4,5,6))