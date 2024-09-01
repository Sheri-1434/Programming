#if and else in Python

#if, elif, if else, else

# x = 200
# if x < 100 :
#     print("first If is True")
# elif x == 100 : 
#     print("Elif is True")
# elif x < 200 :
#     print("Second Elif is True")
# else :
#     print(False)

# print("Exit!!!")

# y = 15
# if y == 15 :
#     print("First Statement is True")
#     print("Desired Statement")
# else :
#     print("First Statement is Wrong")

# print(f"First Statement is {y}")

# var = 23
# print(True) if var != 23 else print(False)

# x = int(input("Enter a Number:"))
# y = int(input("Please Enter Another Number:"))

# if x | y:
#     if x < y:
#         print(int(x + y))
#     elif x == y:
#         print(int(x / y))
#     elif x % y:
#         print(int(x - y))
#     else:
#         print ("No one is elegible to calculate")
# print("Calculated Succesfully")



operation = input("Select an oprator :n ")

for x in operation:
    if "+" not in operation and "-" not in operation and "*" not in operation and "/" not in operation :
        print("syntax Error")
        break
    num1 = input("Enter num1 ")
    num2 = input("Enter num2 ")

    if operation =='+':
        print(int(num1) + int(num2))
    if operation =='-' :
        print(int(num1)- int(num2))
    if operation =='*':
        print(int(num1) * int(num2))
    if operation == '/':
        print(int(num1) / int(num2))

