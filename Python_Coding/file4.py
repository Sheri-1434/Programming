#Class 4: Variable Input and Output

#Output

#Printing mutiple code lines in one line and using #sep and #end Parameters

x= "Sheraz"
y= "Malik"

print(x, y, sep='_')

print("Hi", "Hello", 'How are you')

print("Hi", "We", "are", "writing", "multiple", "outputs", "on", "one", "line", sep='_')
print("Hi", "We are writing multiple code lines")

print("Hi", "We are writing multiple outputs on one line", end=', ')
print("Hi", "We are writing multiple code lines")

#Concatenation use (only doable in case of string)

name = "Sheraz"
age = "21"
print("My Name is "+name , "and my age is "+age)

#format() use 

print(f"My Name is {name} and my age is {age}")

X = 10
Y = 20
Z = 30
A = X*Y*Z

print(f"The sum of {X} {Y} {Z} is {A}" )

#Input 

#var = input("First Name:")
#var2 = input("Last Name:")
#var3 = input("Age:")

#print(f"My Name is {var} {var2} My age is {var3}")

var4 = int(input("a="))
var5 = int(input("b="))
var6 = int(input("c="))
var7 = var4+var5+var6
print(f"The sum of all is = {var7}")




