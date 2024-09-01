# python List: [] --> List 
 
# python has 4 built in datatypes to store data collection, List, Tuple, Set, Dictionaries (All have slightly different traits) 
 
# List, program write in Array ["obj", ....], list() constuctor, also used to create lists

# lists can be ordered , changeable (mutable), duplicate....

# we can update, add and remove objects from lists

#lists have some built in functions for differnet purposes: 


# var = ["apples", "bananas", 1, 4, True, False, "Fruits"]
# var1 = list(("apples", "bananas", "vegetables", "cucumbers", "cakes"))

# Add an item in the list, by replcaing the respective item in the list

# var[3] = 'mango'

# append(), add an item as the end of the list

# var.append("grapes")

#insert , add item in list at a speicified place , insert(index, "item")

# var.insert(0, "Apples")

# pop(), remove a specified item pop(value), otherwise, remove the last item by default

# var.pop(1)

# remove(), remove the provided item from the list remove("item")

# var.remove("apples")

#del function delete the specified index value assign to item from list

# del var[1]

# print(var)
# print(var1)

# Looping in Lists

# for x in var:
#     print(x)


# _var = [12, 120, 100, 110, 100, 200]
# l = len(_var)
# i = 0

# while i < l:
#     print(_var[i])
#     i+=1

# marks = [12, 120, 100, 110, 100, 200]
# max = marks[0]

# for x in marks:
#     if x > max:
#         max = x
# print(max)


# even_numbers = [2, 3, 4, 5, 7, 8, 9, 11, 17, 20, 18]
# even = []

# for x in even_numbers:
#     if x % 2 == 0:
#         even.append(x)
# print(even)

#list Comprehension:

#if we want to put out even numbers or any desired result from a list then we can use loop , but there is a dedicated unique way to print it

# i.e any_variable = [any expression for expression in iterable if condiiton == True] 
# expression refers to the current item in list, also is the outcome of the list, it also manipulate the list ,before the outcome of end item of the list
#iterable can be any objext like (tuple, list, set)
# range is used to make the intergers iterable.


# even_numbers = [2, 3, 4, 5, 7, 8, 9, 11, 17, 20, 18]
# _even = [even for even in even_numbers if even%2 == 0]

# multiply lists
# print(_even * 5)

# Chaging list items using index number:

#if inserted value is < items replaces, then it will insert replace items at specified place and move rest values accoirdingly


# var = ['apples', 'grapes', 'oranges', 'mangoes', 'plums', 'pears', 'blackcurrant']
# var[1:2]  = ['guava', 'percia melon']

#if inserted value is > items replaces, then it will insert replace items at specified place and {delete the indeces which lefts, after replacing} move rest values accordingly

# var1 = ['apples', 'grapes', 'melons', 'mangoes', 'plums', 'pears', 'blackcurrant']
# var1[1:5] = ['apricot', 'pomegrante']
# print(var)
# print(var1)

# Add list items.

#list Types

#insert(): add items at the specified place in the list:

# var = ['apples', 'grapes', 'oranges', 'Plums']
# var.insert(0, "Mango")
# print(var)


#extend(): Add any iterable object (tuple, set, dictioneries, at the end of the list items):

# var = ['apples', 'grapes']
# var1 = ("mangoes", "tomatoes")
# var2 = {'beet-root', 'plums'}
# var.extend(var1)
# var.extend(var2)

# del function remove the specified value
# del var[1]
# # del var
# print(var)


#remove list items

#clear(), will empty all list items adn left []
# var.clear()
# print(var)


#sort(), sort all list items in alphabeticall otder, by default in  ascending order,
# if sort(reverse=True), results in desending order of list items.

# var = ["apples", "bananas", "fruits", "palms", 'apricot']
# var.sort(reverse=True)
# print(var)

#reverse, Reverse the order of list items

# var = ["apples", "bananas", "fruits", "palms", 'apricot']
# var.reverse()
# print(var)

# sort(), by default is case sensitive, in case of uppercase items, results unexpectedly
# buil in key function can get rid of this, sort(key=str.lower)

var = ["apples", "bananas", "Fruits", "Palms", 'apricot']

var.sort(key=str.lower)

# copy: Copy the items and create a new list, list(), slice [:] also uses to copy list.  list.copy(arg)

var1 = list.copy(var)

#join the list: here we can concatenate two lists with different methods, simply, list1 + list2, using extend(), and using append

# var2 = var+var1

# var.extend(var1)

# for x in var1:
#     var.append(x)
# print(var)

# if is use key=str.lower, no matters where i inserted the item , it will be sorted in lowercase, alphabetical order
var.insert(5, "Avocado")
var.reverse()
print(var)
print(var1)
# print(var2)
