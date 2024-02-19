def menu():
    print("Phonebook")
    print("1.Add")
    print("2.View")
    print("3.Update")
    print("4.Remove")
    print("5.Exit")
    print("Enter your option")
    
def add():
    name=input("Enter the name: ")
    Dict[name] = {}
    Dict[name]['email'] = input("Enter the email: ")
    Dict[name]['phone'] = int(input("Enter the phone number: "))
    print(Dict)
    
def view():
    view=input("Enter the name to search: ")
    if view==Dict[]:
       return Dict[]
    else:
       print("Not present in the phonebook")
def update():
    pass
def remove():
    pass


Dict = { }
flag=True

while flag==True:
    menu()
    n=int(input())
    name={}
    if n==1:
       add()
    elif n==2:
       view()
    elif n==3:
       update()
    elif n==4:
       remove()
    else:
       break
       
