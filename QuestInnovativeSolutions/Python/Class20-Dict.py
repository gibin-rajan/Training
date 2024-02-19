# #Dictionary
# a={}            #Empty dictionary
# print(a)
# print(type(a))

# b={ 'name':'xyz', 'age':22,'email':'xyz@mail.com','place':'yyy'}
# print(type(b))
# print(b)

# #Orderd
# #Mutable
# #duplicate not allowed

# b={ 'name':'xyz', 'age':22,'email':'xyz@mail.com','place':'yyy','age':21}
# print(b)

# #length

# b={ 'name':'xyz', 'age':22,'email':'xyz@mail.com','place':'yyy','age':21}
# print(len(b))

# #accessing dictionary items

# b={ 'name':'xyz', 'age':22,'email':'xyz@mail.com','place':'yyy','age':21}
# print(b['email'])
# print(b['name'])

# #second method- get()
# print(b.get('age'))

#Keys  - return list of all key elements in dictionary
# print(b.keys())     #returns keys as tuples inside a list
# print(b.values())   #returns values as tuples inside a list
# print(b.items())    #returns items as tuples inside a list

#membership

# b={ 'name':'xyz', 'age':22,'email':'xyz@gmail.com','place':'yyy'}
# print('age' in b)

#updates values in a dict

# b={ 'name':'xyz', 'age':22,'email':'xyz@mail.com','place':'yyy'}
# print(b)
# b['name']='yxz'
# print(b)
# b['age']=20
# print(b)

#update()-inbuilt method

# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com','place':'yyy'}
# c.update({'email':'zyx@gmail.com'})
# print(c)

#Add items to dictionary
# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
# c['place']='abcd'
# print(c)

#using update method
# c.update({'gender':'male'})
# print(c)

#Remove items from the dictionary
# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
# c.pop('age')
# print(c)

#popitem- remove last items from the dict
# c.popitem()
# print(c)

#clear()
c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
del c['age']
del c       #delete the dict
c.clear()   #reutrns empty dictionary
print(c)

