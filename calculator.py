from tkinter import *
krish=Tk()
exp=""
krish.geometry("400x450")
krish.config(bg="white")

def press(key):
    global exp
    exp+=str(key)
    dis.set(exp)
    
def  equal():
    global exp
    result=str(eval(exp))
    dis.set(result)
def clear():
    global exp
    exp=""
    dis.set("")
        
       
    
dis=StringVar()

display=Entry(krish,font=("times",30,"bold"),textvariable=dis,bg="white")
display.grid(columnspan=5)


one=Button(krish,text="1",font=("Arial",20,"bold"),height=2,command=lambda: press(1),relief="flat",bg="white")
one.grid(row=1,column=0,sticky="nsew",padx=2,pady=10)

two=Button(krish,text="2",font=("Arial",20,"bold"),height=2,command=lambda: press(2),relief="flat",bg="white")
two.grid(row=1,column=1,sticky="nsew",padx=2,pady=10)

three=Button(krish,text="3",font=("Arial",20,"bold"),height=2,command=lambda: press(3),relief="flat",bg="white")
three.grid(row=1,column=2,sticky="nsew",padx=2,pady=10)

foure=Button(krish,text="4",font=("Arial",20,"bold"),height=2,command=lambda: press(4),relief="flat",bg="white")
foure.grid(row=1,column=3,sticky="nsew",padx=2,pady=10)

plush=Button(krish,text="+",font=("Arial",20,"bold"),height=2,command=lambda: press("+"),relief="flat",fg="green",bg="white")
plush.grid(row=1,column=4,sticky="nsew",padx=2,pady=10)


six=Button(krish,text="5",font=("Arial",20,"bold"),height=2,command=lambda: press(6),relief="flat",bg="white")
six.grid(row=2,column=0,sticky="nsew",padx=2,pady=2)

seven=Button(krish,text="6",font=("Arial",20,"bold"),height=2,command=lambda: press(7),relief="flat",bg="white")
seven.grid(row=2,column=1,sticky="nsew",padx=2,pady=10)

eight=Button(krish,text="7",font=("Arial",20,"bold"),height=2,command=lambda: press(8),relief="flat",bg="white")
eight.grid(row=2,column=2,sticky="nsew",padx=2,pady=10)

nine=Button(krish,text="8",font=("Arial",20,"bold"),height=2,command=lambda: press(9),relief="flat",bg="white")
nine.grid(row=2,column=3,sticky="nsew",padx=2,pady=10)

minus=Button(krish,text="-",font=("Arial",20,"bold"),height=2,command=lambda: press("-"),relief="flat",fg="green",bg="white")
minus.grid(row=2,column=4,sticky="nsew",padx=2,pady=10)


five=Button(krish,text="9",font=("Arial",20,"bold"),height=2,command=lambda: press(5),relief="flat",bg="white")
five.grid(row=3,column=0,sticky="nsew",padx=2,pady=10)



zero=Button(krish,text="0",font=("Arial",20,"bold"),height=2,command=lambda: press(0),relief="flat",bg="white")
zero.grid(row=3,column=1,sticky="nsew",padx=2,pady=10)

mul=Button(krish,text="*",font=("Arial",20,"bold"),height=2,command=lambda: press("*"),relief="flat",fg="green",bg="white")
mul.grid(row=3,column=2,sticky="nsew",padx=2,pady=10)

ans=Button(krish,text="=",font=("Arial",10,"bold"),height=2,command=equal,bg="green",fg="white",width=10)
ans.grid(row=4,column=3,padx=2,pady=10,sticky="nsew")

ans=Button(krish,text="clear",font=("Arial",10,"bold"),height=2,command=clear,fg="white",width=10,bg="red")
ans.grid(row=4,column=0,columnspan=3,sticky="nsew",padx=2,pady=10)


div=Button(krish,text="/",font=("Arial",20,"bold"),height=2,command=lambda: press("/"),relief="flat",bg="white",fg="green")
div.grid(row=3,column=4,sticky="nsew",padx=2,pady=10)

per=Button(krish,text="%",font=("Arial",20,"bold"),command=lambda: press("%"),relief="flat",bg="white",fg="green")
per.grid(row=3,column=3,sticky="nsew",pady=10)

clear=Button(krish,text=".",font=("Arial",20,"bold"),command=lambda: press("."),relief="flat",bg="white",fg="green")
clear.grid(row=4,column=4,sticky="nsew",pady=10)
krish.mainloop()
