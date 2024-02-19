#pass by value / call by value

# def new(x):
#     print(x)
#     x=25
#     print(x)
# n=20    #var copy created
# new(n)  #x value doesnt affect the n value because it uses a copy of varriable
# print(n)

#call by reference / pass by reference

# def new(x):
#     print(x)
#     x[0]=25
#     print(x)
# a=[1,2,3,4,5]    #original data is passed to function
# new(a)           #x value does affect the n value because it uses a original data
# print(a)         #[25] original value will be changed after updation

# recursion - function call itself
# 5= 5+4+3+2+1

# def rcrsn(x):
#     if x<=0: #-1
#         return x
#     else:
#         return x+rcrsn(x-1)
#         #3+rcrsn(2) #3+2+rcrsn(1) #3+2+1+rcrsn(0)
# a=int (input("Enter a number"))
# print(rcrsn(a))
#line 30 or 32-33
# z=rcrsn(a)
# print(z)


#Work
# 5= 5*4*3*2*1
# Write fectorial program using recursion
# Write fibonacci series using recursion

# def sq(x):
#     return x*x
# print(sq(x=int(input("Enter the number"))))

#Lambda Function - anonymous function
# Syntax
# lambda arguments : expressions(operation)

x=lambda a : a*a
print(x(6))
