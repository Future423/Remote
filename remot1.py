from tkinter import messagebox  
from tkinter import *
import Weathern2
import nnotepad
import ncalcultor
import pyautogui
from tkinter.filedialog import*
import time

root = Tk()
root.geometry("500x500")
root.title('Remote')
root.config(bg="azure")
root.resizable(0,0)

def INF():
    messagebox.showinfo('Info','Created by Harshita, Sidharth and Nishant')
def INF2():
    messagebox.showinfo('Help','For FAQs or help contact harshitabroka2002@gmail.com/')
def qit():
    root.destroy()   
#menu-bar
mnu= Menu(root)
m1=Menu(mnu,tearoff=0)
m1.add_command(label='Info',command=INF)
m1.add_command(label='Help',command=INF2)
m1.add_command(label='Exit',command=qit)
mnu.add_cascade(label='Options',menu=m1)
root.config(menu=mnu)

#button......

def hi():
    Weathern2.main()

def note():
    nnotepad.ran()
    
def p2p():
    ncalcultor.col()
    
def tk_ss():
    root.iconify()
    time.sleep(0.3)
    ss=pyautogui.screenshot()
    sp=asksaveasfilename()
    ss.save(sp+"_ss.png")

b1=Button(root,text='Weather Report',font="caladea 22",bg="#fff",command=hi)
b1.place(x=20,y=25)
b2=Button(root,text='Notepad',font="caladea 22",bg="#fff",command=note)
b2.place(x=200,y=80)
b3=Button(root,text='Screen Shot',font="caladea 22",bg="#fff",command=tk_ss)
b3.place(x=300,y=100)
b4=Button(root,text='Calculator',font="caladea 22",bg="#fff",command=p2p)
b4.place(x=300,y=25)

root.mainloop()
