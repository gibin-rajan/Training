#list
# a = [1,2,3,4,5]
# print(type(a))

# b = ['abc','def','ghi']
# print(type(b))

# c = [1,'abc',2,'def']
# print(type(c))
# print(c)

#ordered
#mutable-change ,add and remove items
#duplicates is allowed
# a = [1,2,3,4,5,1,1,1,1]
# # print(a)
# print(len(a))

#list() 
# s = (1,2,3,4)
# s = ('abc','def')
# x = list(s)#convert to list
# print(type(x))
# print(x)

#access list items
# a = [1,2,3,4,5,1,1,1,1]
# print(a[0])
# print(a[6])#access using index position
# print(a[-7])#access using negative index position
# print(a[2:5])#normal slicing
# print(a[-5:-1])#negative slicing
# print(2 in a)

#Change item in a list
# a = [1,2,3,4,5,1,1,1,1]
# a[0]=10#update using index position
# a[-2]=12#update using negtv indexing
# a[1:3]=[20,50]#update using slicing
# a[1:3]=[10,20,30,40]#update values and will insert rest values
# print(a)

#add items to a list
# a = [1,2,3,4,5,1,1,1,1]
# # b=(1,2,3)
# # a.append(b)#can insert multiple values but will be in a seperate()
# a.append(12)
# print(a)

# b = ['abc','def']
# b.append('ghi')
# print(b)

#insert()
# a = [1,2,3,4,5,1,1,1,1]
# a.insert(1,50)
# print(a)

#extend()
# a = [1,2,3,4,5,1,1,1,1]
# b = (7,8,9)
# a.extend(b)
# print(a)

#Remove items from a list
# a = [1,2,3,4,5,1,1,1,1]
# # a.remove(3)
# a.remove(1)
# print(a)

# a = [1,2,3,4,5,1,1,1,1]
# # a.pop()#remove last index position
# a.pop(2)#remove according to index position
# print(a)

#del keyword
# a = [1,2,3,4,5,1,1,1,1]
# del a[0]
# del a
# a.clear()#returns an empty list
# print(a)