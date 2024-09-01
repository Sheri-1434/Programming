# Python Modules:

#Modules: A pre-written code that we can use later stores in .py file contains any type of data

#1 Built-in Modules: Python has numerous built-in mudules that we can simply import and use as per our requirement

# import math

# var1 = math.pow(10, 3)
# print(int(var1))


# we can use aliases for renaming modules for conveinent use of any module. (as)

#.pow used to calculate power of first arg ** 2nd arg (x, y)

# import math as m


# var1 = m.pow(10, 3)
# print(int(var1))


# finding squreroot

# var2 = m.sqrt(16)
# print(int(var2))

# pi , will return value of pi, constant

# var3 = math.pi
# print(var3)


#using from during import for only parts import using , as alias

# from math import sqrt, pow


# var4 = pow(2,5)
# print(int(var4))

#sqrt returns the sqrt of any specified value

# var5 = sqrt(36)
# print(int(var5))

# dir(), used to prit all the fucntions, classes all types of vaiables in the specific module


# var6 = dir(math)
# print(var6)


#min and max, find min and max value in an ITERABLE:

# var7 = min(4,8,12,16,20,24,28, 30*4)
# var8 = max(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 20*8)
# print(var7)
# print(var8)

#return absolute (positive) value of a specified value:

# var9 = abs(-245)
# print(var9)


#.ceil and floor () both will raise upward and downward value respectively rounds the value to nearest integer

# var10 = math.ceil(1.45)
# var11 = math.floor(4.3)
# print(var10, var11)


#date and time module:

import datetime


#datetime.datetimee.now() will return the current date and exact time as per the respective time standard


# var12 = datetime.datetime.now()
# print(var12)


#Create a date using datetime(), constructor of datetime module which takes 3 args...(year, month, day)


# var13 = datetime.datetime(2024, 9, 1)
# print(var13)

#strftime() returns datetime object  as readable string, using format function which with 1 arg to specify format of returned string
# we can also get more specific results using other options on module (year, day, month etc...)
  

# print(var13.year)
# print(var13.strftime("%A"))  #print day   
# print(var13.strftime("%a"))  #print short form of day   
# print(var13.strftime("%B"))  # print month
# print(var13.strftime("%C"))  # print century
# print(var13.strftime("%D")) #print in date/month/year
# print(var13.strftime("%w"))  #print week day as number 0-6, 0 for Sunday
# print(var13.strftime("%d"))  #print date of month   
# print(var13.strftime("%b"))  #print shortname of month
# print(var13.strftime("%m"))  #print month a number // 1-12  
# print(var13.strftime("%y"))  #print year in short //24
# print(var13.strftime("%Y"))  #print Year in full //2024


# Time Module

# import time

# # var14 = dir(time)
# _var14 = time.ctime() //current time
# # print(var14)
# print(_var14)


#Python Random Module:

#random module, import any random int between two args provided (x, y) 

import random

# var1 = dir(random)
# print(var1)

# will print random integer value between the provided args random.randint(arg1, arg2)

var2 = random.randint(12, 40)
print(var2)


random.seed(23, 2)
print(random.random())