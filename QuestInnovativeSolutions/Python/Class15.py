#List Operators
#+
# l1=[1,2,3,4]
# l2=[4,5,6]
# print(l1+l2)
# print(l1*3)

# -in
#len()

#Iterate List
# a = [1,2,3,4,5]
# for i in a:
#     print(i)

# a = ['abc','def','ghi']
# for j in a:
#     print(j)

# a = [1,2,3,4,5] #range(5) - 0-4
# for i in range(len(a)):
#     print(a[i])

#While loop use - list iterate

#List sort
# a = [10,5,4,7,16,1]
# a.sort()#ascending order
# print(a)

# a = ['z','r','a','w','p']
# a.sort()#alphabetical order
# print(a)

# a = ['Z','r','a','w','p']
# a.sort()#uppercase char have more priority
# print(a)

# a = [10,5,4,7,16,1]
# a.sort(reverse=True)#descending order
# print(a)

#List reverse
# a = [10,5,4,7,16,1]
# a.reverse()
# print(a)

# b = a.copy()#to create a copy of list
# print(b)

#List Methods
#count()
# a = ['abc','abc','abc','def','gho']
# print(a.count('abc'))#total no of occurence

#index()
# a = ['abc','abc','abc','def','gho']
# print(a.index('abc'))#index position of item

#List Comprehension
# a = ['abc','dca','xya','def','gho']
# b = []
# for i in a:
#     if 'a' in i:
#         b.append(i)
# print(b)

#syntax:
# b = [expression for i in x if condition]
# a = ['abc','dca','xya','def','gho']
# b = [x for x in a if 'a' in x]
# print(b)

#print 1-10 numbers using list comprehension
# a = [i for i in range(1,11)]
# print(a)

# print 10-20 numbers, only print 10-15 using condition
# even numbers in 1-10 numbers using list comprehension
# odd numbers in 15-20 numbers using list comprehension

#Sum of numbers in list [1,2,3,4,5]-15