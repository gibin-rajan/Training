
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox, Progressbar


def new():
    pass
x=Tk()
x.title('Login')
x.geometry('500x300') 

lb=Label(x,text='FirstName')
lb.place(x=10,y=25)

en=Entry(x,bd=5,width=30)
en.place(x=150,y=25)

lb=Label(x,text='Password')
lb.place(x=10,y=75)

en=Entry(x,bd=5,width=30)
en.place(x=150,y=75)

lb=Label(x,text='Gmail')
lb.place(x=10,y=125)

en=Entry(x,bd=5,width=30)
en.place(x=150,y=125)

lb=Label(x,text='Phno')
lb.place(x=10,y=175)

en=Entry(x,bd=5,width=30)
en.place(x=150,y=175)

bn=Button(x,text='Click',command=new)
bn.place(x=200,y=225)
x.mainloop()