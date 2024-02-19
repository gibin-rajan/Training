# # Hierarchial Inheritance 

# class Base:
#     def hello(self):
#         print('Base class')
# class Child1(Base):
#     def frst(self):
#         print('Derived class 1')
# class Child2(Base):
#     def scnd(self):
#         print('Derived class 2')
# obj= Child2()
# obj.scnd()
# obj.hello()
# obj1=Child1()
# obj1.frst()
# obj1.hello()

# #Hybrid Inheritance --Multiple types of inhetitance

# class First:
#     def new(self):
#         print('First class')
# class Second(First):            #Hierarchical inheritance
#     def frst(self):
#         print('Second class')
# class Third(First):
#     def scnd(self):
#         print('Third class')
# class Fourth(Second,Third):     #Multiple inheritance
#     def thrd(self):
#         print('Fourth class')
# obj=Fourth()
# obj.new()
# obj.frst()
# obj.scnd()
# obj.thrd()



# Exception handelling

try:
    age=int (input('Enter your age'))
    print(age)
except:
    print('please enter integer')
    

    
def div(x,y):
    try:
        a=x/y
        print(a)
    except NameError:
        print('Name error')
    # except ZeroDivisionError:
    #     print('cant divide by zero')
    # except:
        print('nait valid')
div(20,5)
div(20,0)