#Pyton While Loop:
# x = 0

# while x <= 50 :
#    print(x)
#    x+=1
# print("Loop executed successfully")


#While Loop Exercise:

#1

# var1 = 1

# while var1 <= 100:
#     print(var1)
#     var1 = var1 + 1
# print("Summed Up All Numbers")

#2

# var2 = 1

# while var2 <= 100 :
#     if var2 % 2 == 0 :
#         print(var2)
#     var2 = var2 + 1
# print('Even Numbers Executed') 

#3

prime = 0
_input = int(input("Enter a Number: "))
var3 = 1

while var3 < (_input):
    if _input % 2 == 0:
        prime = 1
    var3+=1

if prime == 0:
    print(_input, "is a prime number")
if prime == 1:
    print(_input, "is not a prime number")

if prime == 0:
    if _input != 1:
        print("Finally, Prime Numbers Executed")

#4

# x = "aeioudc"

# l = len(x)

# X = 0

# while X < l:
#     if x[X] != "a" and x[X] != "e" and x[X] != "i" and x[X] != "o" and x[X] != "u":
#         print(x[X])
#     X+= 1
# print("Vowels Not Printed")


#5

# var5 = 1

# while var5 <= 20:
#     if var5 % 2 == 1:
#         print(var5)
#     var5 = var5 + 1

# print("Odd Numbers Executed")
