import json
# def FileCreate(filename):
#     with open(filename,"r") as F1:
#         data = json.load(F1)
#     print(data)
# FileCreate('JsonDataFile1.json')
#  -----------------------------------------
# dict = {"name": "John","id": 21,"age": 35}
# print(json.dumps(dict))
#  -----------------------------------------
# x = '{ "organization":"JKTECH","city":"Bangalore","country":"India"}'
# # python object to be appended
# y = {"pin":110096}
# # parsing JSON string:
# z = json.loads(x)
# # appending the data
# z.update(y)
# # the result is a JSON string:
# print(json.dumps(z , indent = 4))

#  -----------------------------------------

# # to update json file JsonDataFile with new record
# def AddRecord(data,filename):
#     with open(filename,"r+") as file:
#         # First we load existing data into a dict.
#         dict = json.load(file)
#         # Join new_data with file_data inside emp_details
#         dict["employee"].append(data)
#         file.seek(0)
#         json.dump(dict,file, indent = 4)
# new_dict = {"name": "John","id": 21,"age": 35}
# AddRecord(new_dict, 'JsonDataFile1.json')
#   -----------------------------------------
# dataDict = {
#     "name": "Sweka",
#     "id": "20",
#     "age": "32"
# }
# with open('JsonDataFile1.json',"a") as file:
#     json.dump(dataDict,file, indent = 4)
#  ---------------------------------------------

dataDict = {     #dictionary data type in python , variable
    "name": "Sweka",
    "id": "20",
    "age": "32"
}
data_json = json.dumps(dataDict)  #convert the dataDict into json string and storing it in data_json
print(data_json)  #printing the json string

data_py_dict = json.loads(data_json) # converting json string to python dict
print(data_py_dict)  #printing the converted  data_py_dict

