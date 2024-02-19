#Printing the Sum of two numbers

a=int(input("Enter the first number "))
b=int(input("Enter the second number"))
print('The sum is',a+b)

#Difference of two numbers

a=int(input("Enter the first number "))
b=int(input("Enter the second number"))
print('The difference is',a-b)

#Find the cube of the number

a=int(input("Enter the number to find cube "))
print('The cube value of ',a,"is",a**3)

#Swap two numbers

a=input("Enter the value of A ")
b=input("Enter the value of B ")
temp=a
a=b
b=temp
print("The value of A after swapping",a)
print("The value of B after swapping",b)


#Find te factorial of two numbers

#Find the largest number of two numbers

a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
if a>b:
    print("First number is the largest number")
else:
    print("Second number is the largest number")

#Find the largest number of three numbers

a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
c=int(input("Enter the third number "))
if a>b and a>c:
    print("First number is the largest number")
elif b>a and b>c:
    print("Second number is the largest number")
else:
    print("Third number is the largest number")

#check the given number even or not

a=int(input("Enter the number "))
if (a%2)==0:
    print("Its even number")
else:
    print("its odd number")

#check the given number odd or not

a=int(input("Enter the number "))
if (a%2)==1:
    print("Its odd number")
else:
    print("its even number")

