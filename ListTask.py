list = ['abc',1,5,6,'hi',34,'def',43,56]

for i in list:   # printing all elements of list
    print(i)
else:
    print("end of list")

for i in list[2:6]:   #slicing
    print(i, end=' ')
print()

for i in range(1,6):  # printing the range of element from 1 to 6 of list
    print(list[i],end= ' ')
print()

list.append(100)  # adding element 100 at the end of list
print(list)  #printing the list

list.pop(3)  # deleting element in the index 3 of list
print(list)

list.insert(4,78)  #insert 78 at 4th index
print(list)

for i in list[:-1]:   #slicing
    print(i, end=' ')
print()

for i in list[1:4]:   #slicing
    print(i, end=' ')
print()

# import cowsay
#
# cowsay.meow("this is cat")
# cowsay.cheese("there you are")
