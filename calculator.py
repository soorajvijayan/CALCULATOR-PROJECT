from tkinter import *

test=Tk()

e=Entry(test,width=34,borderwidth=7,bg="#FFEFDB",fg="#A52A2A")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def add(number):
    
    current=e.get()
    e.delete(0,END)  
    e.insert(0,str(current)+str(number))
    
def clear():
    e.delete(0,END)
def sum():
    f=e.get()
    global fnum
    global math
    math="addition"
    fnum=int(f)
    e.delete(0,END)
def equal():
    num=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,fnum + int(num))
    if math=="subtraction":
        e.insert(0,fnum - int(num))
    if math=="multiplication":
        e.insert(0,fnum * int(num))
    if math=="division":
        e.insert(0,fnum / int(num))            
def sub():
    f=e.get()
    global fnum
    global math
    math="subtraction"
    fnum=int(f)
    e.delete(0,END)

def mul():
    f=e.get()
    global fnum
    global math
    math="multiplication"
    fnum=int(f)
    e.delete(0,END)

def div():
    f=e.get()
    global fnum
    global math
    math="division"
    fnum=int(f)
    e.delete(0,END)

b0=Button(test,text="0",padx=40,pady=20,command=lambda:add(0))
b1=Button(test,text="1",padx=40,pady=20,command=lambda:add(1))
b2=Button(test,text="2",padx=40,pady=20,command=lambda:add(2))
b3=Button(test,text="3",padx=40,pady=20,command=lambda:add(3))
b4=Button(test,text="4",padx=40,pady=20,command=lambda:add(4))
b5=Button(test,text="5",padx=40,pady=20,command=lambda:add(5))
b6=Button(test,text="6",padx=40,pady=20,command=lambda:add(6))
b7=Button(test,text="7",padx=40,pady=20,command=lambda:add(7))
b8=Button(test,text="8",padx=40,pady=20,command=lambda:add(8))
b9=Button(test,text="9",padx=40,pady=20,command=lambda:add(9))
ba=Button(test,text="+",padx=39,pady=20,command=sum)
be=Button(test,text="=",padx=91,pady=20,command=equal)
bc=Button(test,text="clear",padx=79,pady=20,command=clear)
bsub=Button(test,text="-",padx=41,pady=20,command=sub)
bmul=Button(test,text="*",padx=40,pady=20,command=mul)
bdiv=Button(test,text="/",padx=40,pady=20,command=div)

b9.grid(row=1,column=2)
b8.grid(row=1,column=1)
b7.grid(row=1,column=0)

b6.grid(row=2,column=2)
b5.grid(row=2,column=1)
b4.grid(row=2,column=0)

b3.grid(row=3,column=2)
b2.grid(row=3,column=1)
b1.grid(row=3,column=0)

b0.grid(row=4,column=0)

ba.grid(row=5,column=0)
be.grid(row=5,column=1,columnspan=2)
bc.grid(row=4,column=1,columnspan=2)

bsub.grid(row=6,column=0)
bmul.grid(row=6,column=1)
bdiv.grid(row=6,column=2)



test.title("calculator")


test.mainloop()