# Python Fuctions:

# we can use function without passing argument and calling return

# def func1():
#     print("First Function!!!")
#     print("First Function Executed")
# func1()
# func1()

#with argument and calling return


# def func2(a,b):
#     s = a + b
#     print("s=", s)
#     print("Second Function!!!")
#     return func2


# func2(20, 30)
# x = 10
# y = 20
# func2(x, y)


# Default Argument: we don't have need to pass argumnet while recalling function
# if we add value to first argument instead of other it wil through error, so add to the right hand side args.

# def func3(a=30, b=20, c=40):
#     print(a + b + c)
#     return func3

# func3()
# func3(30, 50)
# func3(100, 500)
# x = 30
# y = 40
# z = 30
# func3(x, y, z)

#pass: use for empty body of fucntion, it prevents to return error

# def func4():
#     pass
#     print(func4)

#keyword Argument: Use keywords to assign values ex, c=20, if we dont add keyword with value and with others
# will return errror:

# def func5(a, b, c):
#     print(a + b + c)
#     return func5

# func5(a=10, b=30, c= 20)

#Arbitrary Keyword: (*args): will return all values in a tuple 
# if assign an argument it wil return other values on a tuple except numebr of args assigned

# def func6(*args):
#     print("The number at index2 is",args[2])
#     return args

# func6(10, 20, 30, 40, 50, 60, 70, 80)
# # print(func6[2])

# Arbitrary keyword Argument: (**args) will return all values in a dictionery:

# def func7(**args):
#     print("The value at index 0 is ", args["a"])
#     return args

# func7(a=10, b= 20, z= 30)


# functions can contain any DatatType, (list, tuple, set, dict)

# def func8(items):
#     for x in items:
#         print(x)
# fruits = ["apples", "Bananas", "cherry", True, 5]
# func8(fruits)


#position only arguments:, add , / after arguments and it will execute position only arguments, any other will return error

# def func9(x, /):
#     print(x)

# func9(3)
    

# keyword only arguments: add *, before arguments and it will execute keyword only arguments, any other will return error

# def func10(*, x):
#     print(x)

# func10(x=1)

#combine both keyword-ony and position only (x, y, /, *, z, a )

# def func11(x, y, /, *, z, a):
#     print(x+y+z+a)

# func11(5, 6, z=6, a=10)


# Recursive Fucntion:

# def print_rec( i ):
# 	if i <= 5 :
# 		print("Hello World!")
# 		print_rec( i+1 )	
# 		return 
# 	else:
#             return 

# print_rec( 1 )

def tri_recursion(k):
  if k < 6:
    result = k + tri_recursion(k + 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(1)



