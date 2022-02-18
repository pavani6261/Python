# # In Python, an anonymous function is a function that is defined without a name.
# #
# # While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
# #
# # Hence, anonymous functions are also called lambda functions.
#

# #Compact syntax for writing functions that return one expression
# # Program to show the use of lambda functions
# double = lambda x,y: y / x   #lambda 5:5*2
# double1= lambda z:z*z
# print(double(25,5))
# print(double1(10))
#
# # We use lambda functions when we require a nameless function for a short period of time.
# # In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
# # Lambda functions are used along with built-in functions like filter(), map() etc.
#
# # Program to filter out only the even items from a list
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
#
# new_list = list(filter(lambda x: (x%2 == 1) , my_list))
# new_list1 = tuple(filter(lambda x: (x%2 == 0) , my_list))
#
# print(new_list) #list of odd numbers
# print(new_list1) #tuple of even numbers

# sequences = [10,2,8,7,5,4,3,11,0, 1]
# filtered_answer = filter (lambda x: x > 6, sequences)
# filtered_answer1 = filter (lambda x: x > 6, sequences)
# print(list(filtered_answer))# prints numbers >6 in list format
# print(tuple(filtered_answer1)) # prints numbers >6 in tuple format
# #
# # Program to double each item in a list using map()
#
# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
#
# new_list = list(map(lambda x: x * 4 , my_list))
# # new_list = list(map(lambda x: x > 4 and x < 12  , my_list)) # Relational and Logical returns Boolean value
#
# print(new_list)
#
# #Note that the Lambda functions can have any number of arguments but they have only one expression.
# # Firtsly, the expression is evaluated and then returned.
# # Using return
# def multiplyBy(n):
#     return lambda x: x * n
#
# double = multiplyBy(2)
# triple = multiplyBy(3)
# times10 = multiplyBy(10)
# print(double(4))
# print(triple(4))
# print(times10(4))

# #reduce()
# from functools import reduce
# sequences = [1,2,3,4,5,6]
# product = reduce (lambda x, y: x*y, sequences) # 1*2 =2*3=6*4=24*5=120*6=720
# print(product)
#
# from functools import reduce
# sequences = [1,2,3,4,5,6]
# product = reduce (lambda x, y: x+y, sequences)
# print(product)

from  functools import reduce
list = [1,2,3,4,5,6,7]
prod = reduce(lambda x,y:x*y,list)
print(prod)