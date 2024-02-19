#file handelling
def add(a,b):
    c=a+b 
    # print(c)
    return c

add(2,4)
add(3,29)
add(33,4)
m=add(3,5)
print(m)
if m%2==0:
    print('even')
else:
    print('odd')
    

#keyword arguments
def func(name,message):
    print("printing the message",name,"and the message is",message)

func('john','hello')
func('hello','john')
func(name='john',message='hello')
func(message='hello',name='john')


#default arguments---->when the parameter predefined then it wont return error it take predefined value if you give another value it will use that value

def add(a,b=7):
    print(a)
    print(b)
add(4)
add(3,2)

#required arguments-->should pass two parameters

def add(a,b):
    print(a)
    print(b)
add(4,5)


