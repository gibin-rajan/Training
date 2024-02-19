# QUESTION no 27 to 40

# Accept 10 Element in array with and without loop
#using for loop
n = int(input("Enter number of elements : "))
lst = []
for i in range(n):
    ele = int(input())
    lst.append(ele)
print(lst)

# #using list comprehension
n=int(input("Enter the array size"))
lst1 = [i for i in range(n)]
print(lst1)



# reverse an array

n=int(input("Enter number of elements : "))
lst = []
for i in range(n):
    ele = int(input())
    lst.append(ele)
print(lst)
lst.reverse()
print(lst)

# sum of the elements in the array

a=[2,3,4,5,6]
sum=0
for i in range(len(a)):
    sum+=a[i]
print(a)
print(sum)

# addition of two arrays

a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a+b)

# find the largest Element in the array

n=int(input("Enter number of elements : "))
lst = []
for i in range(n):
    ele = int(input())
    lst.append(ele)
print(lst)
x=0
for i in range(len(lst)):
    while lst[i]>x:
        x=lst[i]
print(x)

# sort array in ascending Order

n=int(input("Enter number of elements : "))
lst = []
for i in range(n):
    ele = int(input())
    lst.append(ele)
print(lst)
lst.sort()

# search element in the array

a=[2,3,4,5,6]
n=int(input("Enter the element to search "))
print(n in a)

# Enter 2 array and check if array are same or not 

a=[1,2,3,4,5]
b=[1,2,3,4,5]
a.sort()
b.sort()
if a==b:
    print("The arrays are same")
else:
    print("The arrays are not same")


