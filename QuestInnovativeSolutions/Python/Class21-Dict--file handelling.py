#Iteration
#Without inbuilt method

# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
# for i in c:
#     print(i)
#     print(c[i])

#With inbuilt method
# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
# for i in c.keys():      #we can use values() also
#     print(i)

# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
# for i in c.items():
#     print(i)
    
# c={ 'name':'xyz', 'age':22,'email':'xyz@mail.com'}
# x=c.copy()      #create a copy of a dictionary
# print(x) 
    
    
#Nested Dictionary
# newclass={'batch1':{'name':'abc','age':10},'batch2':{'name':'def','age':20}}
# print(newclass )
# print(newclass['batch1'])

#fromkeys() -->reurn dict with specified key and value

# x=('first','second','third')
# y=(1,2,3)
# z=dict.fromkeys(y,x)
# print(z)


# Work
# Enter number of employees: 2   -no of iteration

# Enter name :
# Enter salary:
    
# Enter name:
# Enter salary:
    
# output:
# Name is ------- and his salary is -------
# Name is ------- and his salary is -------




#FILE HANDELLING

# open(filename,mode)
# mode 4 -read(r),apppend(a), write(w), create(x)
# t-default
# b-binary mode(files, image)

# f= open('Class/Class19.py','r')         #determine the path of file and file name
# print(f)
# print(f.read())
# print(f.read(10))       #read some limited character
# print(f.readline()) #read one line
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()       #the file sould be closed if its open

#append mode
# f= open('Class/Class19.py','a')
# f.write("appended")         #add at the end of existing line
# f.close()

#write mode
# f= open('Class/Class19.py','w')
# f.write('added')        #it'll remove the exiting content fro the file and write the new content in that file--like overwrite
# f.close()

#create mode
f=open('Class22.py','x')

#delete a file
import os
os.remove('Class22.py')
