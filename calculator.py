from tkinter import*
import math
import tkinter as tk

root = Tk()
root.title("Scientific calculator")
def button_click(val):
    exp =entry.get()
    if val=="C":
        exp=exp[0: len(exp)-1]
        entry.delete(0,END)
        entry.insert(0,exp)

    elif val=="CE":
        entry.delete(0,END)

    elif val== "+":
        entry.insert(END,"+")
        return

    elif val== "-":
        entry.insert(END,"-")
        return

    elif val== "x":
        entry.insert(END,"*")
        return

    elif val== "÷":
        entry.insert(END,"/")
        return

    elif val== "x\u02b8":
        entry.insert(END,'**')
        return

    elif val== "=":
        ans = eval(exp)
        entry.delete(0,END)
        entry.insert(0,ans)
             
    else:
        entry.insert(END,val)
        return

root.config(bg="White")
root.geometry('365x395+500+180')
root.resizable(width=False,height=False)
entry= Entry(root,width=20,borderwidth=20,bg='#003366',fg="white",justify='right',font=('ariel',18,'bold'))
entry.grid(row=0,column=0,columnspan=6,pady=3)
      
button_list=["C" ,"CE" ,"x\u02b8" ,"÷" ,
             "7" ,"8" ,"9" ,"x" ,
             "4" ,"5" ,"6" ,"-" ,
             "1" ,"2" ,"3" ,"+" ,
             "00" ,"0" ,"." ,"="]

row_value=1
col_value=0
           
for i in button_list:
        if(i in "012345678900"):
              button= Button(root,text =i,width=7,font=("ariel",12,"bold"),bg='#0033FF',fg='white',bd=8,height=2,command=lambda button=i:[button_click(button)])
        elif(i=="CE" or i=="C"):
                   button= Button(root,text =i,width=7,font=("ariel",12,"bold"),bg='#03AC13',fg='white',bd=8,height=2,command=lambda button=i:[button_click(button)])
        elif(i=="="):
                   button= Button(root,text =i,width=7,font=("ariel",12,"bold"),bg='#FF0000',fg='white',bd=8,height=2,command=lambda button=i:[button_click(button)])
        elif(i in "+-x÷"):
                   button= Button(root,text =i,width=7,font=("ariel",12,"bold"),bg='#A1045A',fg='white',bd=8,height=2,command=lambda button=i:[button_click(button)])
        else:
           button= Button(root,text =i,width=7,font=("ariel",12,"bold"),bg='#680C87',fg='white',bd=8,height=2,command=lambda button=i:[button_click(button)])
     
        button.grid(row=row_value,column=col_value)
        col_value+=1
        if col_value>3:
            row_value+=1
            col_value=0

root.mainloop()