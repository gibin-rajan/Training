# #index()
# from traceback import format_exc
# from turtle import forward


# a='hello how are you'
# print(a.index('z'))         #if not found returns error

# #format()
# a='hello how are you'
# b=10
# print(a.format(b))   

# #using placeholder
# a='hello how are you .. my age is{} ..my height is{}.. my weight is{}..'
# b=10
# c=145
# d=111
# print(a.format(b,c,d))

# #using positional argument
# a='hello how are you .. my age is{2} ..my height is{0}.. my weight is{1}..'
# b=10
# c=145
# d=111
# print(a.format(b,c,d))

# #using keyword argument
# a='hello how are you .. my age is{c} ..my height is{d}.. my weight is{b}..'
# print(a,format(b=22,c=104,d=155))

# #i want to pay 200 for 10 to 20 items format using positional arguments
# a='i want to pay {0} for {1}to{2} items'
# b=200
# c=10
# d=20
# print(a.format(b,c,d))

# n=50
# f=12.0
# s='hello'
# print("The value is %d..value is %f..my string is %s"%(n,f,s))
# print("my %d age"%(n))

# a='python'
# print(a.isalpha())
# print(a.isdecimal())
# print(a.islower())
# print(a.isupper())
# print(a.lower())
# print(a.upper())


# #Ljust-->Left justification
# a='python'
# x=a.ljust(25)        #it create 25 spaces from left
# print(x,"is easy")

# #Rjust-->Right justification
# a='python'
# x=a.rjust(25,0)     #it create 25 '0' from right
# print(x,"is easy")


# x=a.lstrip()        #remove the empty spaces from the left
# y=a.rstrip()        #remove the empty spaces from the right
# print(x)
# print(y)


# #replace
# a='hello xx'
# print(a.replace('l','x'))

# x=a.swapcase()
# print(x)

# a='python'
# x=a.zfill(10)       #if the string doesnt have 10 character it add 00 at the front
# print(x)


# #work
# #write a program to check if the word 'hello' present in 'hello how are you,
# #Find the first and last occurence of the letter 'o' in 'Hello world'

# #Qn 18
# #Qn 26