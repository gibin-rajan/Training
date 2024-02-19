# Encapsulation or data hiding 

# class A:
#     __z=10        #Properties   #Double underscore used to make variable private 
#     def neww(self):
#         # print(self.z)       #we cannot access directly the variable so we can use one of the two properties
#         # print(A.z)
#         print(A.__z)          #private variable can be accessed within the class
# obj=A()
# obj.neww()
# print(obj.__z)      #cannot be accessed outside the class
# print(A.__z)        #cannot be accessed outside the class


#private method 

# class B:
#     def __init__(self):
#         B.__new(self)
#         # self.__new()
#     def __new(self):          #private method
#         print("Data hiding")
# obj1=B()
# # obj1.__new()                #cannot be called outside



# Abstraction

# ABC --Abstract Base Class
# abstractmethod




from abc import ABC,abstractmethod
class First(ABC):
    def __init__(self,name):
        self.n =name
    def hello(self):        #normal method
        print(self.n)
    @abstractmethod
    def abs(self):          #abstract class
        pass

class Second(First):
    def abs(self):
        print("Welcome",self.n)
    def new(self):
        print("Neewwww")
obj =Second('ammu')
obj.abs()
obj.new()
# obj.hello()