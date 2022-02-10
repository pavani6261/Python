# import json
# emp = '{"name":"joe","id":"67" }'
# emp_dict = json.loads(emp)
# print("json string is",emp_dict)
#
# print("python object to json string:",json.dumps(emp_dict))

import json
# {key:value mapping}
a ={"name":"John",
    "age":31,
    "Salary":25000}

# conversion to JSON done by dumps() function
b = json.dumps(a)
# printing the output
print(b)
print(repr(b))
print("type of a:",type(a))
print("data type of b:",type(b))