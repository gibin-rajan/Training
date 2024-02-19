# Regular expression 

import re

# search()-- returns a match obj if match found else done
# text='Hello how are you... How is your day'
# x=re.search('how',text)
# print(x)

# findall()--returns a list containing all matches else empty list
# text='Hello how are you... How is your day'
# x=re.findall('How',text)
# print(x)

#split()

# text='Hello how are you... How is your day'
# x=re.split('o',text,2)  #''-determine where should the text split  ,after text we can determine how many time it should split 
# print(x)


#sub()
# text='Hello how are you... How is your day'
# x=re.sub('o','today',text,2)        #first string is the word to be replaced and the second string is a new word,after text we can determine how many time it should replace 
# print(x)


# Metacharacters
# []-to print range of characters
# text='Hello how are you... How is your day'
# x= re.findall('[a-e]',text)
# print(x)

# \d --return the numbers in the string
# text='2Hello how 3are you... How 4is your day'
# t=re.findall('\d',text)
# print(t)

# .--return the given thing
# i.e ex.  (h.w)--in this it check the word start with h and end with w but it will take one word inside because of single dot
# text='Hello how are you... How is your day'
# x= re.findall('h.w',text)
# print(x)

# ^--Starts with
# text='Hello how are you... How is your day'
# x= re.findall('^H',text)
# print(x)

# $--endswith
# text='Hello how are you... How is your day'
# x= re.findall('y&',text)
# print(x)

# *
# text='Hello how are you... How is your day'
# x= re.findall('o*',text)
# print(x)

# *--zero or more occurence

# text='Hello how are you... How is your day'
# x= re.findall('ow*',text)       ##  it will check the character starts o and ow
# print(x)

# +--one or more occurence  it only check the character 'ow'
# text='Hello how are you... How is your day'
# x= re.findall('ow+',text)       #  it only check the character 'ow'
# print(x)

# {}--specifies the character in between just like '.'
# text='Hello how hellw are you... How is your day'
# x= re.findall('h.{3}w',text)
# print(x)


# |--either one of them or
# text='Hello how are you... How is your day'
# x= re.findall('are|zz',text)
# print(x)
