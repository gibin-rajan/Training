# from Class27 import hello
# hello('python')


# from Class27 import add
# # print("enter the number")
# # a=int(input())
# # b=int(input())
# # print(add(a,b))

from Class27 import *   # *-used to import all the files from the corresponding file
print(a)
print(a['name'])
print(a['place'])

from math import *  # math-used to import all the predefined math functions and methods from the corresponding file
# import math

print(factorial(5))
print(sqrt(4))

import random
print(dir(random))  #complete methods
list=[1,2,3,4,5]
print(random.choice(list))  #random item select
r1=random.randint(5,10)     #range of values, one item will be selected randomly
print(r1)
print(random.random())      #0-1 floating point randomly
random.shuffle(list)        #change the position of the list items
# x = (1,2,3,4)             #shuffle not working in tuple,set,dict
# random.shuffle(x)
# print(x)
print(list)