from tkinter import *
from tkinter import messagebox
import random

win=Tk()

win.title("PASSWORD GENERATOR")

win.geometry("644x434")
win.minsize(861,404)
win.maxsize(861, 404)



def cal_sum():
   t1=int(a.get())
   t2=str(b.get())
   lower_case = "abcdefghijklmnopqrstuvwxyz"
   upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   numb = "1234567890"
   speical_char = "!@#$%^&*"

   something = lower_case + upper_case + numb
   everithing = lower_case + upper_case + numb + speical_char
   if t2 == 'yes':
    password = "".join(random.sample(everithing,t1))
    
   elif t2 == 'no' :
       password = "".join(random.sample(something,t1))
    
   else:
       password = "Enter the valid character" 
       messagebox.showerror("Error","Enter valid character") 
   

   label.config(text=password,state="normal")


Label(win, text="Enter The Length ", font=('Calibri 13')).pack()
a=Entry(win, width=35)
a.pack()
Label(win, text="For special character type(yes/no)", font=('Calibri 13')).pack()
b=Entry(win, width=35)
b.pack() 

label=Label(win, text="GENERATE PASSWORD", font=('Calibri 25'))
label.pack(pady=20)

Button(win, text="Generate", command=cal_sum).pack()

win.mainloop()