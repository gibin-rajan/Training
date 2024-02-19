# display square of even numbers from 1-10 

# a=[i**2 for i in range(1,11) if i%2==0]
# print(a)

# # numbers from 1-100 that are divisible by 6

# a=[i for i in range(1,10) if i%6==0]
# print(a)

# #convert lowercase strng to uppercase using list comprehension

# n=str(input("Enter a string"))
# a=[i.upper() for i in n]
# print(a)

# remove all vowels in a string 

n=str(input("Enter a string"))
a=['a','e','i','o','u','A','E','I','O','U']
b=[i for i in n if i not in a]
print(b)

#Matrix
# a = [[1,2],[2,4]]#2*2
# print(a)
# b = [[1,2,3],[4,5,6]]#2*3

# a = [[1,2],[2,4]]
# b = len(a)
# # print(b)
# for i in range(b):#range(2)-0,1
#     print(a[i])

#Addition of 2matrix
# a = [[1,2],[2,4]]
# b = [[1,0],[1,4]]
# c = [[0,0],[0,0]]
# for i in range(len(a)):#0  #1
#     for j in range(len(b)):#0 #1
#         c[i][j]=a[i][j]+b[i][j] #[2 #2] [3,8]
# print(c)
# for i in range(len(a)):#0  #1
#     for j in range(len(b)):#0 #1
#         print(c[i][j],end=' ')
#     print()

#matrix using input
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
        print(c[i][j],end='')
    print()