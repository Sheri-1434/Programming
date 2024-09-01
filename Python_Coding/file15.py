# Python Set: {} --> representation

#set is unordered, unchageable, and not duplicate the items, unindexed

cities = {"Islamabad", "Lahore", "Karachi", "Hyderabad", "Rawalpindi", "London", "California"}

# No duplciation is allowed

# NOTE: True and 1 are considered as same values, False and 0 are declared as same, so printed the first occurence, 

cities1 = {"California", "London"}
cities2 = {"copenhegen", "Hertferdshire", 2}


# set(), also used to create set

countries = set(("Pakistan", "USA", "UK", "Australia"))

# Accessing set items using for loop, As we cant use while loop , bcz we cant do indexing

# for x in cities:
#     print(x)

# for y in countries:
#     print(y)

# check items if exist:

# if "Islamabad" in cities:
#     print(cities)


# add(),  We can still add itemds in set 

# cities.add("Gujranwala")


# update(), used to add one set into another , can be any iterbale objects(list, tupels, sets, dict  etc)
# will only change the original set set, nor return a new set, not return duplicate items

# countries.update(cities)

#union(), use to add all set an return a new set, we can add multiple sets to add in one union (set1, set2, set3....)
# Allows to add tuple and lists to sets, will not return duplicate items

# c_1 = cities.union(countries)

# c_1 = cities.union(countries, cities1, cities2)


# or we can use "|" for adding, both results same, or multiple sets can be added same way
# only adds sets with sets

# c_1 = cities | countries | cities1 | cities2


#intersection(), will return same items of sets only, 

# c_1 = cities.intersection(cities1)


# & also does the same job, but btw sets only

# c_1 = cities & cities1

# intersection_udpate(), will only change the original set set, nor return a new set, return only same  items of sets

# cities.intersection_update(cities1)

#difference(), will return items of set1 that are not in set 2, in a new set, exclude duplicates

# c_1 = cities.difference(cities1)


# - also does the same job, but btw sets only

# c_1 = cities - cities1

#difference_updates(), will only change the original set, nor return a new set, return only items of set1 not in set2

# cities.difference_update(cities1)


#symmetric_difference:  will return items that are NOT in both sets , in a new set, exclude duplicates

# c_1 = cities.symmetric_difference(cities1)

# ^ also does the same job, but btw sets only

# c_1 = cities ^ cities1

#symmetric_difference_update(): will only change the original set, nor return a new set, return only items of that are not present in bth sets

# cities.symmetric_difference_update(cities1)

#copy(), copy all items and return new set

# c_1 = cities.copy()


# c_1 = cities.isdisjoint(cities1)
# c_2 = cities.issubset(cities1)
# c_3 = cities.issuperset(cities1)


#remove() and discard(), both are same but if removing item doesn't exists, remove Will raise error,
# while discard WIll NOT raise error

# countries.remove("USA")
# countries.discard("London")

#pop(), will remove a random item as we dont know the index, bcz set is unordered

# countries.pop()

#clear(), will return empty set

# countries.clear()

# print(cities)
# print(countries)
# print(cities1)
# print(c_1)
# print(c_2)
# print(c_3)