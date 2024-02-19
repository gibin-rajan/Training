# Polymorphism 




# Method overiding 

class Ab:
    def abc(self):
        print('Welcome')
class De(Ab):
    def abc(self):          #same function name for parent class and child class. in that case for which class we create object that class method is called . we can avoid this by using super keyword
        print('second')
    def deg(self):
        print('new')
obj=De()
obj.abc()
obj.deg()



def p(a,b):
    print("hiii")
def p(a,b,c):
    print("heloo")
p(1,2)          #This thorw an error
p(1,2,3)        #this will run because two func name are same so it prefer lastly created function

# Operator overloading 

#adddition
class A:
    def __init__(self,a):
        self.n=a 
    def __add__(self,s):
        return self.n+s.n 
obj1=A(2)
obj2=A(3)
print(obj1+obj2)        #A.__add__(obj1,obj2)

#substarcation
class A:
    def __init__(self,a):
        self.n=a 
    def __sub__(self,s):
        return self.n+s.n 
obj1=A(2)
obj2=A(3)
print(obj1-obj2)        #A.__sub__(obj1,obj2)

# Comparison
class A:
    def __init__(self,a):
        self.n=a 
    def __lt__(self,other):
        if self.n<other.n:
            print("obj1 is lesser")
        else:
            print("obj2 is lesser")
obj1=A(2)
obj2=A(5)
if obj1<obj2:
    pass