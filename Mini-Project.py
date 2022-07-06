from tkinter import *
from tkinter import messagebox
import random as r
def button(frame):          
    b=Button(frame,padx=1,bg="light blue",width=3,text="   ",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b
def change_a():
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break
    def reset():                
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" " 
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])
