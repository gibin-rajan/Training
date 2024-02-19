#Work
#1. check person is eligible to vote or not

Age=int(input("Enter your age "))
if Age>=18:
    print("You are elegible to vote.")
else:
    print("You are not eligible to vote.")

#2.
#mark 85 - 100 : grade - A
#mark 75 - 85 : grade - B
#mark 65 - 75 : grade - C
#mark 55 - 65 : grade - D
#mark 45 - 55 : grade - E
# failed 

mark=int(input("Enter your mark "))
if mark>85:
    print("Your grade is A")
elif mark>75:
    print("Your grade is B")
elif mark>65:
    print("Your grade is C")
elif mark>55:
    print("Your grade is D")
elif mark>=45:
    print("Your grade is E")
else:
    print("You have failed in this exam")

#3.odd numbers in first 10nos

a= int(input(" Please Enter the Value : "))
i=1
while i<=a:
    if(i%2==1):
        print(i)
    i=i+1



#4.even numbers in first 10nos

a= int(input(" Please Enter the Value : "))
i=1
while i<=a:
    if(i%2==0):
        print(i)
    i=i+1


