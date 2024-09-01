# Python Classes/Objects

# Class is a constrcutor for creating objects, or like a blueprint

# class MyClass():
#     x = 10
#     y = 20
#     z = x + y

# # c1 = MyClass()
# print(MyClass())

# __init__ will called automatically once class is initiated
# __str__ ,controls what to execute if we are using stings in obejct properties
# self parameter(should be the first parameter), refers to the values in the object, can be any anything ex, abc, Person, Cities

class Class():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Python is a {self.x} {self.y}"
        
var = Class("Programming", "Languauge")

# Modify the value of Object Properties 

var.x = "High-Level"                    
print(var)


#del the object properties

# del var.x                                   
# print(var.x)


# del the object

# del var
# print(var)


# Class cant be empty but incases we can use pass function to prevent any error

class objects():
    pass