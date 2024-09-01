# Python File Handling

# we can create , write and delete file , using some methods

# r: Open file for read only - throughs error if file doesn't exists
# a: Open file for appending - crate file if doesn't exists
# w: Open fiel for writing - Create file if doesn't exists, WILL OVERWRITE EXISING CONTENT
# x: Create file with specfied name - throughs error IF FILE EXISTS

var = open("testing.txt", "w")

var.write("This is 1st line\n")

# "w"

var.write("This is 4th line\n")

# "a"

var = open("testing.txt", 'a')
var.write("This is 5th line\n")

# read file, read() read upto you want, ALSO WE CAN SPECIFY THE LENGTH WE WANT TO READ, readline(), to read the whole line

var = open('testing.txt', 'r')
# print(var.readline())
print(var.read())


# "x", open new file , if file exists throughs error

# var = open("test1.txt", 'x')
# var.write("ANother test file")
# var.write("Second line")


# delete the file, import os module first then .remove() for file and remove folders (removedirs) if empty, if contain files throughs error

# import os

#use conditions to avoid any error

# if os.path.exists("testing.txt"):
#     os.remove("testing.txt")
# else:
#     print(False)

# os.removedirs("D:\Programming\Testing_Folder")



# it is a good practice to close files after done with writing, // may not add new data because of buffering

# var.close()
