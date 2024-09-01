# Python User Defined Modules:

# import my_modules.first_module

# import importlib

# importlib.reload(my_modules.first_module)       # used to reload a module, means import it again

# import my_modules.first_module

# var1 = my_modules.first_module.fruits_list
# # print(var1)

# var2  = my_modules.first_module.func1(10, 8)
# print(var2)

# var_ = dir(first_module)
# print(var_)



# Python Pip

# Pip is pakcage manager in python use pip command to install various packages of python for different usages.


# Python Packages,  A set of modules grouped together


# Numpy used to work with arrays, In Numpy array are called ndarray, also its type cahnge to ndarray



import numpy as np

var1 = np.array((10, 20, 40 ,50 , 100))
print(var1)

#ndim : return numebr of dimension in array
#ndmin: ste number dimension to return


var2 = np.array([1,2,3,4])
var3 = np.array([1,2,3,4], ndmin=5)
print(var2)
print(var2.ndim)
print(var3)
print(var3.ndim)


# Plays audio file that you have provided as you run the code, 

# import audioplayer

# audioplayer.AudioPlayer("Play.ht - Sales !!!🚀🚀🚀.wav").resume()