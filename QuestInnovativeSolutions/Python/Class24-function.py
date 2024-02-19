# #variable lengh arguments

# def add(*a):            #for variable length argument we use * symbol   
#     print(a)
#     print(type(a))
#     s=0
#     for i in a:
#         s=s+i
#     print(s)            #for the sum of the arguments
        
    
# add(1,2,3,4,5,4)        #it wont return error it will pass the arguments as tuple format


# #local and global variable

# b=1            #global variable
# def show(a):
#     v=10       #local variable
#     print(v)
#     print(a)
#     global b   #likethis
#     b=b+5      #cannot modify directly like this should use global keyword before that  -- and b hold this value 
#     print('inside',b)

# print('outside',b)  #now the value of b is 1  
# show(5)
# # print(v)       #cannot access outside the function 
# print('outside',b)  #now the value of b is 6 because of function call before this




lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)

