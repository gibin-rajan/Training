# class A:
#     'docstring'     #documentation string           #just like comment we can get by line no:9
#     def __init__(self):
#         pass
#     def frst(self):
#         print('success')
# obj=A()
# obj.frst()
# print(A.__doc__)    #return documentation string   #its only works on first line only after the class   
# print(A.__dict__)   #return all the dictionaries of the class
# print(A.__name__)   #return class name 
# print(A.__module__) #return modules from the class

# # Attribute methods 

# class A:
#     a=10
#     b=20
# obj1=A()
# # print(A.a)
# # print(obj1.a)
# z=getattr(obj1,'a')
# print(z)
# y=hasattr(obj1,'d')
# print(y)
# x=setattr(obj1,'d',30)
# print(obj1.d)
# u=delattr(obj1,'a')
# print(obj1.a)

# # Instance variable and  instance method

# class Student:
#     def __init__(self,a,b):
#         self.x=a        #instance variable
#         self.y=b
#     def avg(self):      #instance method
#         return (self.x+self.y)/2
# obj=Student(10,20)
# print(obj.avg())

# # Class variable and class method 

# class Employee:
#     empname='aaa'       #class variable
#     empid=101
#     def __init__(self):
#         self.name='abc'
#         self.age=12
#     @classmethod
#     def details(cls):
#         print(Employee.empname,' ',Employee.empid)
# obj=Employee()
# obj.details()
# # Instance variable -- object level variable
# # Class variable --class level variable

# # Static method 

class Emp:
    def __init__(self):
        pass
    @staticmethod
    def add(a,b):
        print(a+b)
obj=Emp()
obj.add(5,10)

# # 