#change tuple value
a=(1,2,3,4,5,1,1,1)
a[0]=20
print(a)

#add items to tuple
a=(1,2,3,4,5,1,1,1)
# tuple-->list
# inbuilt methods
# list-->tuple

#remove items from tuple
del a       #delete complete tuple
print(a)

#packing and unpacking tuple
a=(1,2,3)   #packing a tuple
(x,y,z)=a
print(x)
print(y)
print(z)

#loop
a=(1,2,3,4,5,1,1,1)
for i in a:
    print(i)
    
for i in range(len(a)):
    print(a[i])

#while

a=(1,2,3,4,5,6)
i=0
while i<len(a):
    print(a[i])
    i=i+1
    
#join tuple
a=(1,2,3,4,5,1,1,1)
b=(4,5)
print(a+b)
print(a*2)      #repeat multiple times

#tuple methods
#count()--no of times value occur in tuple
a=(1,2,3,4,5,1,1,1)
print(a.count(1))

# index()--position
print(a.index(3))


#sets
a={}
print(type(a))      #it returns dictionary

#sets
a=set()         #empty set
print(type(a)) 
print(a)     

#unordered
#immutable(not able to update)
#no duplicates allowed

a= {1,2,3,4,5,1,1,1,1}
print(type(a))
print(len(a))
print(a)

d={1,2,3}
s=set(d)        #convert to set
print(type(s))


a={1,4,3,2,6,5}     #unorederd returnes sorted list
print(a)




