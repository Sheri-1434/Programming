# Python Exception Handling:
# print("Start"   # // compile time Error, program will  return Error instantly
# x = 10
# y = 0            # runtime Error, program will run and pythin will detect where the error occurs and print it.
# z = x / y
# print(z)
# print("End")


# Use exception hanlders to prevent Errors

# print("Start")  
# x = 10
# y = 0

# here we are  using different conditions to prevennt error, but what if error still there?

# we will use exeptions, try except

# try:
#     if y < 10:
#         print("If")
#         z = x / y
#         print(z)
#     else:
#         print("Else")
#         z = x + y 
#         print(z)

# except  NameError as a:
#         print("Exception Error is = ", a)

# except  ZeroDivisionError as b:
#         print("Exception Error is = ", b)

# except  Exception as c:
#         print("Exception Error is:", c)

# else:
#      print("Else of Except")  # only prints if try is free of errors , True
# finally:
#      print("Finally is Executed")  # regardless of condition it will return, interms of error or without error

# print("End")


# raise, we can raise an exception with whatever we want to raise


# x = (10, 20, 30, "str")
# if x is not int:
#     raise NameError("Sorry, We can't support this format")


class error:
    def __init__(self, arg1):
        self.arg1 = arg1
        try:
            if self.arg1 == 10:
                print("IF")
                print(True)
            else:
                print("Else")
                print(arg1 + a+ b)
        except Exception as error:
            print("Except", error)
        else:
            print("Try is Executed")
        finally:
            print("we have run error handling!!!")
x = error(20)
