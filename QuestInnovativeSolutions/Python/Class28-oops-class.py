#class classname:
    #properties
    #methods
# obj=classname()
# obj=classname()
# obj=classname()
# obj=classname()

# class Person:   #classname needs to be captial
#     pass
# obj1=Person()   #object or instance

class Person:
    x=10
    def method(self):       #should give self bcz of function inside the class
        print("welcome")
obj1=Person()   #object or instance
print(obj1.x)   #property called using object
obj1.method()   #function call
obj1.method()   #function call
obj1.method()   #function call

obj2=Person()
obj2.method()
print(obj2.x)
# del obj2.x
del obj2        #delete object
# print(obj2.x)   #not defined error
obj3=Person()  
obj3.method() 
print(obj3.x)   