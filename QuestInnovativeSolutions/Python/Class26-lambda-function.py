# Adding two numbers
# a = lambda x,y : x+y
# print(a(4,5))

# Multiply 3 numbers using lamda

# a = lambda x,y,z : x*y*z
# print(a(2,3,4))

# Filter() 

# a=[1,2,3,4,5,6,7,8,9,10]
# x= list(filter(lambda n : n%2==0,a))
# print(x)
# print odd numbers in list using lamda
# print the numbers divisible by 6

#map()

a=[1,2,3,4,5,6,7,8,9,10]
x= list(map(lambda n : n**2,a))
print(x)

# Muliply each number with 5 using map

# a=[1,2,3,4,5,6,7,8,9,10]
# x= list(map(lambda n : n*5,a))
# print(x)

# reduce()
# from functools import reduce
# a=[1,2,3,4,5,6,7,8,9,10]
# x=reduce(lambda n,m : n+m ,a)   #1(1st item)+2(2nd item)=3(sum)+3(3rd item)=6(sum)+4(4th item)+......
# print(x)

#reduce() using range()
# from functools import reduce
# z= reduce(lambda n,m :n+m , range(10,20))
# print(z)

#print even number from 20-40 using filter range()

# z=list(filter(lambda n : n%2==0 , range(20,41)))
# print(z)