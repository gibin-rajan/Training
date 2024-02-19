#work 

#even number within range 10-20

# for i in range(10,21,2):
#     print(i)
    
#even numbers sum within range 40-100
# sum=0
# for i in range(40,101,2):
#     sum=sum+i
# print("The sum of the even numbers within range 40-100 is",sum)


#Factorial(qn:7)

# num = int(input("Enter a number: "))
# factorial = 1
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)


#Check number is prime or not(for loop qn:15)

num = int(input("Enter a number: "))
if num > 1:
   for i in range(2,num):
       if num % i == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")

