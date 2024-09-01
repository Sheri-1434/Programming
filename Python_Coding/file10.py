#while Loop Exercises:

# s1 = "Programming Language"
# l = len(s1)
# x = 0

# while x < l:
#     print(s1[x])
#     x+=1

# Examples of While Loop

# sum = 0
# x = 0

# while x <= 15:
#     sum = sum + x
#     x+=1
# print(sum)


# sum = 0
# x = ""
# while x != "N":
#     x = input("Enter number to \'summ up\' or press \'N\' to exit: ")
#     if x != "N":
#         sum = sum + int(x)
# print(sum)


#More Exercises: Class 12, 

#Patterns
# 1             1 2 3 4 5
# 1 2           1 2 3 4 5
# 1 2 3         1 2 3 4 5
# 1 2 3 4       1 2 3 4 5
# 1 2 3 4 5     1 2 3 4 5

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print(j, end = " ")
#         j+=1
#     print()
#     i+=1

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end = " ")
        j+=1
    print()
    i+=1


# i = 1
# while i <= 5:
#     print("* " * i)
#     i+= 1
