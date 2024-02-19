#reverse a number 
# n=int(input("Enter number: "))
# rev=0
# while n>0:
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# print("Reverse of the number:",rev)


#palindrome number

n=int(input("Enter number:"))
temp=n
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
if temp==rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    
#Armstrong Number

# n=int(input("Enter the number"))
# temp=n
# a=0
# while n!=0:
#     d=n%10
#     r=r+d**3
#     n//=10
# if temp==a:
#     print("The number is Armstrong number")
# else:
#     print("The number is not Armstrong number")
    