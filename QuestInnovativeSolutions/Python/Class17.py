# #matrix using input
a = int(input("Enter rows"))
b = int(input("Enter cols"))
c = []
for i in range(a):
    d = []
    for j in range(b):
        e = int(input("Enter elements"))
        d.append(e)
    c.append(d)
print(c)
for i in range(a):
    for j in range(b):
        print(c[i][j],end=' ')
    print()

#matrix addition:

a=int(input("Enter the row"))
b=int(input("Enter the column"))
first=[]
for i in range(a):
    c=[]
    for j in range(b):
        d=int(input("Enter the elements"))
        c.append(d)
    first.append(c)
print("The first matrix",first)

e=int(input("Enter the row"))
f=int(input("Enter the column"))
second=[]
for i in range(e):
    g=[]
    for j in range(f):
        h=int(input("Enter the elements"))
        g.append(h)
    second.append(g)
print("The second matrix",second)

sum=[]
for i in range(a):
    rs=[]
    for j in range(b):
        rs.append(first[i][j]+second[i][j])
    sum.append(rs)
print("The sum is",sum)
# for i in range(len(sum)):
#     for j in range(len(sum)):
#         print(sum[i][j],end=" ")


#Tuple    
a=(1,2,3,4,5)
print(a)
print(type(a))
print(len(a))

b=('a','b','c')
print(type(b))

b=('a','b','c')
print(type(b))
c=tuple(b)      #convert to tuple datatype
print(type(c))

#ordered
#immutable
#duplicates allowed

w='string'
print(type(w))
x=('string')
print(type(x))              #string datatype
z=('string',)
print(type(z))              #tuple datatype

#access tuple
a=(1,2,3,4,5,1,1,1)
print(a[0])          #1
print(a[-2])         #1
print(a[1:4])        #(2,3,4)
print(a[:4])         #(1,2,3,4)
print(a[4:])         #(1,1)


# Qn27-35
# Qn 17
# #number to words
# #0-9
# a=['zero','one','two','three','four',,,,,,'nine']
# #10-20
# a=['ten','eleven',,,,,'nineteen']
# n=int(input("Enter the number"))
# if n<10:
#     print(a[n])
# elif n
