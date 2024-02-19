from tkinter import *
from tkinter import messagebox

x=Tk()
x.title('FirstApp') 
x.geometry('500x300')
lb=Label(x,text='FirstName')
lb.grid()

en=Entry(x,bd=5,width=30)
en.grid(row=0,column=1)
lb1=Label(x,text='Password')
lb1.grid(row=1,column=0)
en=Entry(x,bd=5,show='*',width=30)
en.grid(row=1,column=1)
def new():
    messagebox.showinfo('info','Login Successful')
bn=Button(x,text='Login',command=new)
bn.grid(row=2,column=2) 
x.mainloop()