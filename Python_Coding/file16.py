# Python Disctionaries: {}

# dict are ordered in Pythin 3.7, before this pythin is considered as unordered

#Dict are key:value pairs used to store data

# val1 = {
#     "name": "Sheraz",
#     "age": 21,
#     "country": "Pakistan",
#     # "name1": "Ali"
#     # "age1":  24,
#     # "country1": "Pakistan"
# }

# print((val1))

#dict(), also used to create dict list

# val2 = dict(name = "Ali", age =  24,  country =  "Pakistan")

# print(val2)

# Access dict items


# print(val1["name"])
# print(val1.get("name"))


#key() funtion to print keys of all dicts, values() to print values, items() for priting key:value pair

# print(val1.keys())
# print(val1.values())
# print(val1.items())

# Check if items Exist:

# print("age" in val1)

#Add, Update , Remove Items:

# val1["salary"] = "10 Million"   # if items not exists , it will add a key:value pair

# val1["Gender"] = "Male"         # if items not exists , it will add a key:value pair

# update()

# val1.update({"age" : "23"})     # if items not exists , it will add a key:value pair 
# print(val1)

# pop()

# val1.pop("Gender")
# val1.pop("salary")
# print(val1)

#popitem(), will remove last key:value pair, before Python 3.7. rempoves random values

# val1.popitem()
# print(val1)

# del val1["age"]
# print(val1)


#copy() copies the values of first dict and create a new with same  values

# val3 = val1.copy()
# print(val3)

#Looping in Dictionery

# for x in val1:
#     print(x, "=", val1[x])

# for x in val1.items():
#     (n) = x
#     print("n = ", n)

# Unpacking Dictionary:

# (*n, a) = val1.items()
# print(n)
# print(a)
# print(c)
# print(n1)
# print(n2)


#Nested Dictionares, Adding 3 dicts as nested dicts and return all in once

nested_dicts = {
    "dict1": {
        "name" : "Sheraz",
        "age": 21,
        "country": "Pakistan"
},
    "dict2": {
            "name2": "Ali",
        "age2":  24,
        "country2": "Pakistan"
},
    "dict3" : {
        "name3": "Saad",
        "age3":  23,
        "country3": "Pakistan"
    },
}

# print(nested_dicts)

#Adding 3 dicts to 1 and return a new dict

# dict1 = {
#         "name" : "Sheraz",
#         "age": 21,
#         "country": "Pakistan"
# }
# dict2 = {
#          "name2": "Ali",
#         "age2":  24,
#         "country2": "Pakistan"
# }

# dict3 = {
#         "name3": "Saad",
#         "age3":  23,
#         "country3": "Pakistan"
# }

# dicts = {
#     "dict1" : dict1,
#     "dict2" : dict2,
#     "dict3" : dict3

# }

# print(dicts)


# Access items in nested dicts

# print(dicts['dict3']["name3"])

# Looping in nested dicts

# for x, obj in nested_dicts.items():
#     print(x)
#     for y in obj:
#         print(y, ":", obj[y])


#More Dict Methods:

#fromkeys(), parameters, key and vlaue, key is required: return speicified keys and values assing to them:, if no value provided return None value

# var1 = ("key1", "key2", "key3")
# var2 = ("Dictionary")


# var3 = dict.fromkeys(var1)

# print(var3)

# setDefault: prints value of the specified key, if key doesnt exists, append as new key, if value not assigned return NONE as value
# if value exists then it has no effect 


var1 = {
    "car": "Ferrrari v6",
    "brand": "Ferrari",
    "year": 1997
}

print(var1.setdefault("brand"))