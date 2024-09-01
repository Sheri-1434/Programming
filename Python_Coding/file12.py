# Continue and Break Statements:

# var = "Hello There"

# for x in var:
#     if x in " ":
#         continue
#     print(x)
# print()

# var1 = 1
# while var1 <= 6:
#     if var1 == 3:
#         var1+= 1
#         continue
#     print(var1)
#     var1+=1


# break Statement:

# var2 = 1
# while var2 <= 10:
#     if var2 == 6:
#         break
#     print(var2)
#     var2+=1


var3 = 0

while True:
    _input = input("Enter a number to Add: ")
    if _input == "N":
        break
    var3 = var3 + int(_input)
else:
    print("Breaked")        

print(var3)

