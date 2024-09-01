# Python Scope

#global scope: we can use it both inside and outside function but after coming out of fucntion
# x = 20

# def func():
#     print(x)
# func()

#local scope, where we can only access variable inside of function

# def func1():
#     x = 20
#     print(x)
#     def func2():
#         x = 10
#         print(x)
#     func2()
# func1()


# the value will be refer to global variable value, unless we use global keyword oinside of function


# x = 30

# def func1():
#     global x
#     x = 20
#     print(x)
# func1()
# print(x)

#nonlocal: used wihtin nested functions , to modify the outer function value

def func2():
    x = "Hello"
    def func3():
        nonlocal x
        x = "Carry"
        return x
    func3()
    return x


print(func2())