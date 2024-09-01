# Finding Prime Number Using Function:


# Using while loop

# var1 = int(input("Enter a Number: "))
# i = 0
# is_prime = True

# while i < var1:
#     if var1 % 2 == 0:
#         is_prime = False
#         # break
#     i+=1

# if is_prime == True:
#     print(var1, "is a Prime Number")
# if is_prime == False:
#     print(var1, "is not a prime number")


# Function 

def prime_number(n):

    i = 0
    is_prime = True

    while i < n:
        if n % 2 == 0:
                is_prime = False
        i+=1
    
    return is_prime

n = int(input("Enter a Number: "))

prime = prime_number(n)

if prime:
    print(n, "is a Prime Number")
else:
    print(n, "is not a prime number")


prime = prime_number(32)

if prime:
    print("is a Prime Number")
else:
    print("is not a prime number")


n = int(input("Enter a Number: "))

prime = prime_number(n)

if prime:
    print(n, "is a Prime Number")
else:
    print(n, "is not a prime number")