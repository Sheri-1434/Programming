#Python Strings

# We will goung to cover mulitple usages og strings in python


#we  want to execute multiple lines of strings then we will use triple quotations

#var = "double quotation string"

# var1 = """if we want to execute multiple lines of strings
# then we will use triple quotations"""


#using Array in strings, "in and not in operators", "Slicing" in String, len() function, Escape sequence


# var0 = "Double Quotation String"
# var1 = "Double \"Quotation\" String"

# name = "Sheraz"
# age = 21
# Gender ="Male"

# var2 = "My Name is {0} and my age is {1} and \"iam\" a {2}" 

# print(var0)
# print(var1[-15])
# print("undo" not in var1)
# print(var1[:-16])
# print(len(var1))
# print(var2.format(name, age, Gender))

#String Methods

#capitalize()
var = "captalize the first letter"
#in case of number, it return the same result
Var = "21 is my age"

#casefold(): lowercase the stirng, lower() also does same, but it is more aggressive and find more matches
var1 = "Hi There, Welcome To My WEBSITE"

#center(): centered the string,  two parameters (length, character), length of returned string and character is optional default is space ""

Var1 = "center the string"

#count(): count how many time a value "ex: a" appers in that string , with three parameters, (value, start, end), default start is 0 and end is the ending of string

var2 = "How many a characters are there in this string"

#encode:    encode the string and return provided encoding method, default is UTF-8, with two parameters (encoding, errors), both are optional , 1st returns deault UTF-8, 2nd has different legal values
# backlashreplace, namereplace, ignore, name, strict, replace, xmlcharrefreplace
Var2 = "Encode thå String"

#endswith: check ig the string ends with the specified value, with three parameters (value, start, end), default start is 0 and end is the ending of string, Return Ture or False
var3 = "This string ends with String"

#expandtabs: Add whitespaces between text, one parameter (value), default value is 8

Var3 = "H\ti\tT\th\te\tr\te"

#find(): it will find the index number of specified value and print it, otherwise print "-1", parameters(value, start, end)

var4 = "This is a find string method"

# print(var.capitalize())
# print(Var.capitalize())
# print(var1.casefold())
# print(Var1.center(34, "C"))
# print(var2.count("g"))
# print(var3.endswith("String", 0, 30))
# print(Var3.expandtabs(2))
# print(var4.find("d"))



# print(Var2.encode(encoding= "ascii", errors= "ignore")) #ignore that chracter
# print(Var2.encode(encoding= "ascii", errors= "replace")) #put a questuon mark their
# print(Var2.encode(encoding= "ascii", errors= "namereplace")) #
# print(Var2.encode(encoding= "ascii", errors= "backslashreplace"))
# print(Var2.encode(encoding= "ascii", errors= "xmlcharrefreplace"))
# print(Var2.encode(encoding= "ascii", errors= "strict"))


