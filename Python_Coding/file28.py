# Python Stack Implementation:

#Queue: First Item CAlls at first.
#Stack: First item Calls at last

# stack = []

# while True:
#     var = input("Enter 1 to continue:")
#     if var == "0":
#         break

#     if var == "1":
#         stack1 = input("Enter names to append:")
#         stack.append(stack1)

#     elif var == "2":
#         if len (stack) <= 0:
#             print("No name left to pop")
#         else:
#             x = stack.pop()
#             print(f"Popped name is {x}")
#     else:
#         print("Invalid Response")
#     print(stack)



# Queue:

queue = []

while True:
    var = input("Enter 1 to continue:")
    if var == "0":
        break

    if var == "1":
        stack1 = input("Enter names to append:")
        queue.append(stack1)

    elif var == "2":
        if len (queue) <= 0:
            print("No name left to pop")
        else:
            x = queue.pop(0)
            print(f"Popped name is {x}")
    else:
        print("Invalid Response")
    print(queue)