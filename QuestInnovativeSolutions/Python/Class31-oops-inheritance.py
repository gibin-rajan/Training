# class Stud1:
#     def __init__(self,d,e):
#         self.d=d
#         self.e=e
#     def prnt(self):
#         print(self.d,self.e)
# class Stud2(Stud1):
#     def __init__(self, a,b):
#         # Stud1.__init__(self,a,b)      #passing value through sub class to superclass method 1
#         super().__init__(a,b)           #passing value through sub class to superclass method 2
# obj1=Stud2('abc','def')
# obj1.prnt()


# Multilevel Inheritance 

class Person1:
    def helo(self):
        print("welcome")
class Person2(Person1):
    def new(self):
        print("OOPS concept")
class Person3(Person2):
    def frst(self):
        print("Inheritance")
class Person4(Person3):
    def scnd(self):
        print("Multilevel Inheritance")
obj=Person4()
obj.scnd()
obj.frst()
obj.new()
obj.helo()


# Multiple Inheritance 


class PersonA:
    def frst(self):
        print("welcome")
class PersonB:
    def scnd(self):
        print("OOPS")
class PersonC(PersonA,PersonB):
    def thrd(self):
        print("Multiple Inheritance")
obj1=PersonC()
print(PersonC.__mro__)      #Method Resolution Order --- Check order of inheritance
obj1.thrd()
obj1.scnd()
obj1.frst()


#class work
# ṃathematical prgm 


class Addition:
    def __init__(self,c,d):
        self.c=c
        self.d=d
    def add(self):
        print(self.c+self.d)
class Substraction(Addition):
    def sub(self):
        print(self.c-self.d)
class Multiplication(Substraction):
    def mul(self):
        print(self.c*self.d)
class Division(Multiplication):
    def __init__(self,a,b):
        super().__init__(a,b)
    def div(self):
        print(self.c/self.d)
object=Division(4,2)
object.add()
object.sub()
object.mul()
object.div()

