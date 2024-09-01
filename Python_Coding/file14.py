# Python Tuples: () --> Tuple

# var1 = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')

# var2 = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')
# Var = var1 + var2
# del var1


# var2 = tuple(('Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun', var1))

# if tuple have one item in it then add "," after the item ex. ("Item",)
# var3 = ('January',) 



#tuple is directly unchangeable, but we can do it by converting it into list and then back to tuple
# using list and tuple constructors respectively

# var1 = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')

# var_1 = list(var1)
# print(var_1)
# var_1.append("Sat")
# var_1.append('Sun')
# print(var_1)
# var_1 = tuple(var_1)
# print(var_1)


# Unpacking tuple
# We can map items in tuple to variable , but variables should be equal to number of items, otherwise it returns an error.


var1 = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')

# (day1, day2, day3, day4, day5) = var1


#looping in Tuple:

# Var = ('Mon', 'Tue', 'Wed', 'Thur', 'Fri')
# i = 0
# l = len(Var)
# for x in Var:
#     if x == 'Wed':
#         continue
#     print(x)

# while Var:
#     print(Var)
#     Var+=1

# print(day1)
# print(day2)
# print(day3)
# print(day4)
# print(day5)

# print(Var)
# print(var_1)
print(var1.count("Fri"))
print(var1.index("Fri"))
