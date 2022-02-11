import csv

## creating a csv file in this python folder
# with open('FirstCsvFile.csv',"w", newline='') as Cfile:
#     w1 = csv.writer(Cfile)   # writting into the file using writer()
#     w1.writerow(["Id","Name","Branch"])  #writting each list as a row in the file using writerow()
#     w1.writerow(["23", "Somu", "CSE"])
#     w1.writerow(["25", "Ram", "EEE"])

##opening the csv file of python folder in read mode
# with open('FirstCsvFile.csv',"r", newline='') as Cfile:
#     Data = csv.reader(Cfile,delimiter =' ' )  #reading from the file using reader() in csv. delimiter=' ' replace ' ' with comma
#     for row in Data:
#         print(' '.join(row))
#
## creating csv file in particular path
# with open("C:\\CsvFiles\\FirstCsvFile.csv", "w") as file1:
#     w1 = csv.writer(file1)  #writting in to the file which is opened with writer() in csv
#     w1.writerow(["Id","Name","Branch"])  # writting list in to the file row by row with writerow()
#     w1.writerow(["21", "Somu", "CSE"])
#     w1.writerow(["22", "Ram", "EEE"])
#     w1.writerow(["23", "Ram", "EEE"])

## opening file in read mode
# with open("C:\\CsvFiles\\FirstCsvFile.csv", "r") as file1:
#     data = csv.reader(file1, delimiter=' ')
#     for row in data:
#         print(''.join(row))


## creating csv file in particular path and to write multiple records at once
#using 2 dimensional list we can do it
# CsvList = [["Id","Name","Branch"],["21", "Somu", "CSE"],["22", "Ram", "EEE"],["23", "Amy", "ECE"]]
# with open("C:\\CsvFiles\\FirstCsvFile2.csv", "w") as file1:
#     w1 = csv.writer(file1)  #writting in to the file which is opened with writer() in csv
#     w1.writerow(CsvList)  # writting list in to the file row by row with writerow()

##
##CSV file where we want to write to
##fieldnames - a list object which should contain the column headers specifying the order in which data should be written in the CSV file
## Using DictWriter() writting dictionary data into csv file
with open("C:\\CsvFiles\\FirstCsvFile2.csv", "w", newline= '') as file2:
    Headingnames = ["Name","Id"]
    w2 = csv.DictWriter(file2, fieldnames=Headingnames)
    w2.writeheader()
    w2.writerow({"Name" : "Sam","Id" : "201"})
    w2.writerow({"Name" : "Amy","Id" : "202"})
    w2.writerow({"Name" : "John","Id" : "203"})

# using DictReader() reading the csv file data
#reading it back
with open("C:\\CsvFiles\\FirstCsvFile2.csv", "r") as file1:
    data = csv.DictReader(file1)
    for row in data:
        print(dict(row))   # it gives output in dictionary format
# #-----------------------------
# ##Inheritance in CSV
# # import module
# import csv
#
# class Employee:
#
#     def employeeDetails(self):
#         with open('FirstCsvFile.csv', newline='') as csvfile:
#             data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in data:
#                 print(', '.join(row))
#
# class Department(Employee):
#
#     def departmentDetails(self):
#         with open("C:\\CsvFiles\\FirstCsvFile2.csv", newline='') as csvfile:
#             data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#             for row in data:
#                 print(', '.join(row))
#
# obj = Department()
# # output
# print("-----Employee Detail-----")
# obj.employeeDetails()
# print("-----Department Detail-----")
# obj.departmentDetails()