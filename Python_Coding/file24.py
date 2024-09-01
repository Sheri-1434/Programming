# Python Inheritance:

# class Person():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     # def print_sum(self):
#         print("Sum is:", self.x + self.y)

# # var = Person(10, 20)

# class Person2(Person):
#     def  __init__(self, x, y, n, a):
#         super().__init__(x, y)
#         # super().print_sum(x, y)
#         self.n = n 
#         self.a = a
#     def print_all(self):
#         print(self.x, self.y, self.n, self.a)

# var = Person2(10, 20, 30, 40)
# # var.print_sum()
# var.print_all()



# class A:
#   def __init__(self, a):
#     self.a = a

#   def display_a(self):
#     print( " a =", self.a )	

# class B (A):
#   def __init__(self, a, b):
#      super().__init__(a)
#      self.b = b

#   def display_b(self):
#     print( " a =", self.a, " b =",self.b  )	
	
    
# o1 = B(10,20)
# o1.display_a()
# o1.display_b()


# class A:
#   def __init__(self, a):
#     self.__a = a

#   def display(self):
#     print( "a =", self.__a )	

# o1 = A(10)
# print(o1._A__a)
# o1.display()

class A:
  def __init__(self, a):
    self.a = a
  def __sub__(self, x):
    return self.a - x.a


a1 = A(100)
a2 = A(10)
print(a1-a2)



