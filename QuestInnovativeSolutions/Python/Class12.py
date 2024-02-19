# str='Hello'
# str[1]='p'
# print(str)  #we cant change the value in string

# str='Hello'
# str='hi'
# print(str)  #it will print hii because of line by execution


# #delete
# a='Welcome'
# del a[1]
# print(a)      #we cant delete particular word from a string

# del a
# print(a)     #But we can delete whole string using del keyword


# #Update
# str='hello'
# str[1]='p'
# print(str) #we cant update particular character from the string

#String Operators
#concatination

# a='my'
# b='World'
# # print(a+''+b)

# # #repetation
# # print(a*3)
# #in 
# #% String Formating
# print('hello %s hello'%(a,b)) #we can also add integer using %d

# #Escape Sequence
# #\n --->Next line
# print("Hello good morning\n How are you?")
# #\t --->tab space
# print("Hello good morning\t How are you?")
# #\b --->Backspace -remove a word before this command
# print("Hello good morning\b How are you?")
# #\\-->Backslash
# print("Hello good morning\\ How are you?")
# #\""-->Double quote inside a double quotes
# print("Hello good morning\"How are you?\"")
# #\'--->Sinle Quote
# print('Hello good morning\'How are you?\'')

# #string methods 
# #captialize()-->first letter upper case
# a='hello world'
# x=a.capitalize()
# print(x)

# #casefold)-->returns all character to lower case
# a='Hello How are you'
# print(a.casefold())

# #count()-->total number of occurence
# a='Hello How are you'
# print(a.count('l'))

# #startswith()-->Check if string starts with particular char
# a='hello how are you'
# print(a.startswith('h'))

# #endswith()-->Check if string ends with particular char
# a='hello how are you'
# print(a.endswith('you'))

# #find()-->Check if string contains particular char and return its index. if doesnt have that char itll return -1
# a='hello how are you'
# print(a.find('u'))

