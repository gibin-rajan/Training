# tkinter
# GUI-graphical user interface

from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox, Progressbar


x=Tk()                  #creating object for Tk---Tk is a buildin class
x.title('FirstApp')     #to change the name of the title
x.geometry('500x300')   #for the dimention of the window
# print('hii')            #it'll print this keyword in the teriminal
lb=Label(x,text='FirstName',bg='red',fg='yellow',font='Arial')
lb.grid()
#Entry

en=Entry(x,bd=5,width=30)
en.grid(row=0,column=1)
# lb1=Label(x,text='LastName')
# lb1.grid()
lb1=Label(x,text='LastName')
lb1.grid(row=1,column=0)#to specify the position we use row and column
#Entry
en=Entry(x,bd=5,show='*',width=30)
en.grid(row=1,column=1)
# x.mainloop()            #calling of the Tk window
# print('hello')          #this will print after the TK window closed because it's given after mainloop


'''


        Class 38 starting 
        
        
'''

# Tkinter 

# Button 

def new():
    # print('Clicked')                             #print the output in the terminal
    lb1.configure(text='Changed')                  #used to Change the lb1 text element 
    messagebox.showinfo('info','Login Successful') #used to show the message box syntaxis ('title','text')
bn=Button(x,text='Click',command=new)              #used to create the button with a function 'new'  . When we click the button it will run the function new
bn.grid(row=2,column=2)                            #used for an alignment

# Radio button 

first=IntVar()
rn=Radiobutton(x,text='Male',variable=first,value=1)
rn.grid(row=4,column=0)
rn1=Radiobutton(x,text='Female',variable=first,value=2)
rn1.grid(row=4,column=1)
rn2=Radiobutton(x,text='Other',variable=first,value=3)
rn2.grid(row=4,column=2)

# Checkbutton

ch1= Checkbutton(x,text='English')
ch1.grid(row=5,column=0)
ch2= Checkbutton(x,text='Tamil')
ch2.grid(row=5,column=1)
ch3= Checkbutton(x,text='Malayalam')
ch3.grid(row=5,column=2)

# x.mainloop()

# class work
# LOGIN 
# username -entry
# password -entry-hidden
# login button -->message box(Login successful)


'''

        
        Class 39 -- Starting


'''

# tkinter

# Spinbox
sp=Spinbox(x,from_=1,to=50,width=30)
sp.grid(row=6,column=0)

#set value for a spinbox

s =IntVar()
s.set(25)

spin=Spinbox(x,from_=1,to=50,width=30,textvariable=s)
spin.grid(row=7,column=0)

# Scrolledtext 

scr=ScrolledText(x,width=8,height=5)
scr.grid(row=9,column=0)

# Combobox 

cm= Combobox(x,width=6)
cm['value']=('abc','def','ghi',0)
cm.grid(row=10,column=0)
cm.current(0)                       #this will select default value 'abc' because we gave 0
# cm.current(1)                       #this will select default value 'def' because we gave 1

# Progressbar

prg=Progressbar(x,length=500)
prg['value']=70
prg.grid(row=11,column=0)
# x.mainloop()


'''


Class 40 Starting


'''
#Tkinter

# Menu bar

men = Menu(x)           #main menu
filemenu=Menu(men,tearoff=False)        #submenu
men.add_cascade(label='File',menu=filemenu)     # #submenu adding to main menu
filemenu.add_command(label='New file')
filemenu.add_command(label='Open file')
filemenu.add_command(label='save file')
filemenu.add_command(label='Exit',command=x.quit)
filemenu.add_separator()     #to make a seperation
filemenu.add_command(label='Undo')

editmenu=Menu(men,tearoff=False)
men.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
x.configure(men=men)

# alignment
# place 

lb4=Label(x,text='New text',bg='blue')
# lb4.place(x=250,y=280)
lb4.place(relx=0.5,rely=0.2,anchor=NE)          #anchor should be compass direction must be n, ne, e, se, s, sw, w, nw, or center --relx-relative x-----rely-relative y
#relaive position x&y coord(0.0-1.0)

# Pack
lb5=Label(x,text='PackLab1',bg='red')
lb5.pack(ipadx=100,ipady=100)           #internal padding-ipadx,ipady    when we use we shouldnt use the grid method

x.mainloop()