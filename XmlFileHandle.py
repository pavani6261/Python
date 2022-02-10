# from bs4 import BeautifulSoup
# with open('Xml1file.xml','r') as file:  #opening xml file in read mode
#     data = file.read()  #reading the xml data and storing into data variable
#
# pyDict = BeautifulSoup(data,'xml')  #passing the data of xml to xml parser of beautifulsoup
#
# for tag in pyDict.find_all('Product', {'name':'Tv'}): #find_all() is predefined fn used to check all lines in the file
#     tag['price'] = "Hello!!"  #replace the price value to Hello!! in the record wherever key name is tv
# print(pyDict.prettify())  #to display the text same as in xml file with tags

#----------------------------

# import xmltodict
# import pprint
#
# with open('Xml1file.xml','r') as file:
#     data = file.read()
#
# py_dict = xmltodict.parse(data)
#
# pprint.pprint(py_dict, indent = 4)

# ---------------------------------------------

import json
import pprint

import xmltodict

with open('Xml1file.xml','r') as file:
    Data2 = file.read()
    file.close()
pyDict = xmltodict.parse(Data2)
pprint.pprint(pyDict)

JsonDict = json.dumps(pyDict)

with open("Xml_JsonData.json","w") as file2:
    file2.write(JsonDict)
    file2.close()
