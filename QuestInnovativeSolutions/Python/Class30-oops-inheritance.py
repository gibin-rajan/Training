# Destructor 
class Emp:
    a=10
    def __init__(self): #constructor
        print("Created")
    def __del__(self):  #destructor method
        print("Deleted")
obj=Emp()               #automatic control goes to constructor
del obj
print(obj.a)

# Inheritance 

class Student:          #Parent class or base class
    def profile(self):
        print("This is your profile")
        
class Marks(Student):   #Child class or derived class
    def subj(self):
        print("Marks...")
        
obj1=Marks()
obj1.subj()
obj1.profile()


class Person:           #parent class
    def __init__(self,name ,age):
        self.name=name
        self.age=age
    def prnt(self):
        print(self.name,self.age)
class Employe(Person):  #child class
    pass
object=Employe('xxx',10)
object.prnt()
    