# lamba Functions: (Contain multiple arguments but only one expression)

#lambda aguments: expression

# myfunc = lambda a,b: a*b
# print(myfunc(2,3))


#lamda is a anonymous functon whose best use case is in nested inside a fuction and results your desired values

def func1(n):
    return lambda m: n + m

var = func1(4)
print(var(4))


# it is used for short term function usecase, only contain one line syntax
