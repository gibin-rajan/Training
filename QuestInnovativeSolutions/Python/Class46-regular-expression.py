# Special Sequence 
import re

# \A--check string starting with particular character
# text='Hello how are you... How is your day'
# x= re.findall('\AH',text)
# print(x)

# \b 
# text='Hello how are you... How is your day'
# x= re.findall(r'\bo',text)--starts with
# # x= re.findall(r'a\b',text)--ends with
# print(x)

# \B
# text='Hello how are you... How is your day'
# # x= re.findall('\Be',text)
# x= re.findall('i\B',text)
# print(x)

# \d --return the numbers in the string
# text='2Hello how 3are you... How 4is your day'
# t=re.findall('\d',text)
# print(t)

# \D 
# text='2Hello how 3are you... How 4is your day'
# t=re.findall('\D',text)
# print(t)

# \s--reurn the spaces in the string
# text='Hello how are you... How is your day'
# x= re.findall('\s',text)
# print(x)

# \S-without space it will return the string list
# text='Hello how are you... How is your day'
# x= re.findall('\S',text)
# print(x)

# \w --return the whole string in the list format--it wont take special character
# text='Hello how are you... How is your day @ # $ %'
# x= re.findall('\w',text)
# print(x)

# \w --return the special character only
# text='Hello how are you... How is your day @ # $ '
# x= re.findall('\W',text)
# print(x)

# \Z 
# text='Hello how are you... How is your day'
# x= re.findall('y\Z',text)
# print(x)

# Sets 

# [aHo]-reutrns --check the particular character and returns
# text='Hello how are you... How is your day'
# x= re.findall('[aHo]',text)
# print(x)

# [a-p]--it wont print that range of letters
# text='Hello how are you... How is your day'
# x= re.findall('[a-p]',text)
# print(x)

# [^aHc] -it wont return these characters
# text='Hello how are you... How is your day'
# x= re.findall('[^aHc]',text)
# print(x)

# [a-zA-Z]
# text='Hello how are you... How is your day'
# x= re.findall('[a-zA-Z]',text)
# print(x)

# [0-9]
# text='Hello how are you... How is your day'
# x= re.findall('[0-9]',text)
# print(x)



# tkinter registration(4 fields only) -name --only letters     email-should in this format @gamil.com     ----mobile number only 10 degits  password min 5 (char,digits,spe char) submit button


# text='Hello how are you...how is your day'
# x=re.search("how",text)
# print(x.start())
# print(x.end())
# print(x.span())

# text='Hello how are you...how is your day'
# x=re.search(r"\bH\w+",text)
# print(x.group())

text='Hello how are you...how is your day'
x=re.search(r"\bh",text)
print(x.string)