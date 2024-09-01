# For Loop:

# s1  = "Programming Language"

# for x in s1:
#     print(x)


# Printing vowels in for loop

# s1 = "Python Language"

# for x in s1:
#     if x not in "aeiou":
#         print(x)


#if we dont have body of for loop then we can use "pass" to prevent error

# s1 = "Python Language"

# for x in s1:
#     pass

# for x in range(1, 6):
#     for y in range(1, x + 1):
#         print(y, end = " ")
#     print()


# for loop Exercises:

#1 Print upto 100 numbers using for loop:


# sum = range(1, 100)

# for x in sum:
#     print(x)
#     # print()

#2 Print Even Number from 1 to 100:

   
# sum1 = range(1, 101)     
     
# for y in sum1:    
#     if y % 2 == 0:            
#         print(y)
# else:
#     print("Even Numbers Executed")




# sum1 = range(0, 101, 2)     
     
# for y in sum1:               
#     print(y)
# else:
#     print("Even Numbers Executed")


#3 Print Odd Numbers from 1 to 100:

# sum1 = range(1, 100, 2)

# for y in sum1:      
#     print(y)
# else:
#     print("Even Numbers Executed")


# sum1 = range(1, 100)

# for y in sum1:
#     if y % 2 == 1:      
#         print(y)
# else:
#     print("Odd Numbers Executed")

#4 Print Prime Numbers:

sum1 = str(input("Enter a Number to Check:"))
prime = True

for x in sum1:
    if x % 2 == 0:
        prime = False

if prime == True:
    print(x, "is a prime number")
else:
    print(x, "is not a prime number")


# sum1 = range(1, 100) 

# for y in sum1:
#     if sum1 % 2 == 0:      
#         print(y)
# else:
#     print("Prime Numbers Executed")


#5 Print value excluding vowels:

# var = "Programming Language"
# for x in var:
#     if x not in "aeiou":
#         print(x)