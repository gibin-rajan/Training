# Constructor 
class Emp:
    def __init__(self):     #Constructor
        print("This is a constructor")
    def hello(self):
        print('welcome')
obj1=Emp()  #object or instance of class
obj1.hello()    #method call using object

# Constructor using parameter
 
class Person:
    def __init__(self,name,age):
        print(name,age)
    def hi(self):
        print('welcome')
obj2=Person('xxx',10)
obj2.hi()


class Person:
    def __init__(self,name,age=20):
        # print(name,age)
        self.fname=name
        self.ages=age
    def hi(self):
        print(self.fname,self.ages)  #acccess data using self parameter
        print('welcome')
obj2=Person('xxx',10)
obj2.hi()
obj3=Person('yyy')
obj3.hi()

# Use parameterized constructor , one method for performing operation and another method to print result
# First number = 100
# Second number =200
# Addition = 300

class Addition:
    def __init__(self,n1,n2):
        self.sum=n1+n2
    def add(self):
        print("The sum is",self.sum)
n1=int(input("Enter the first number"))
n2=int(input("Enter the first number"))
obj4=Addition(n1,n2)
obj4.add()

