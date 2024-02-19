# Exception Handelling 

try:
    print('10'+10)
except TypeError:       #its excecuted when given type of error occurs only
    print("Cannot concatinate str and integer")
except:                 #When the error not defined in the except it will run default excecuted
    print('Error')
else:                   #there is no error or when the except block skipped only else block excecuted
    print("No exception eroors")
finally:                #Always executed
    print("Always executed")
    
    
#raise keyword
                    # used to create error by user

# try:
#     age=int(input("Enter the age"))
#     if age>=18:
#         raise
# except:
#     print('Age should be less than 18')



# try:
#     age=int(input("Enter the age"))
#     if age>=18:
#         raise NameError
#     else:
#         print("not greater than 18")
# except NameError:
#     print('Age should be less than 18')
    
# Assertion 

# try:
#     a=5
#     b=10
#     assert a>b,"not greater"
#     print("A is greater than b")
# except AssertionError as m:
#     print(m)

# User defined Exception 

# class AgeError(Exception):      #When we create an user defined exception should inherit class Exception
#     pass
# try:
#     age=int(input("Enter age"))
#     if age<0:
#         raise AgeError
#     else:
#         print(age)
# except AgeError:
#     print("Enter valid age")
    
# Write program to print square of a number using assertion ,if number is less than ) should print error message

# basic qns 41-46 