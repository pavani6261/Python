import array as arr

# a= arr.array('u',['a','b','c'])
# print('array is: ',end = " ")
# for i in range(0,3):
#     print(a[i], end = ' ')
# print()

str = "Hello"
ch = [1,2,3,4,5,6]
a=arr.array('i',ch) # i for interger, d for float
print('array is : ',end = ' ')
for i in (a):
    print(i, end = ' ')
print()

a.insert(3,9)  #  add value= 9 at the index = 3
print("array after insertion: ")
for i in (a):
    print(i, end = " ")
print()

a.append(11)  #  add value at the end of array
print("array after appending: ")
for i in (a):
    print(i, end = " ")
print()

a.pop(3)  # index
print("array after deleting using pop: ")
for i in (a):
    print(i, end = " ")
print()

a.remove(11)   #  value as parameter
print("array after deleting using remove: ")
for i in (a):
    print(i, end = " ")
print()