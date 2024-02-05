from tkinter import*
import random
import string

root = Tk()
root.geometry("800x400")  
root.title("password generator")

def password():
    len=int(Entry1.get())
    lowerD = string.ascii_lowercase
    upperD = string.ascii_uppercase
    digitsD = string.digits
    symbolsD = string.punctuation
    combine  = lowerD + upperD + digitsD + symbolsD
    p= ''.join(random.sample(combine, len))
    Entry2.delete(0,END)
    Entry2.insert(0,p)

    

l1=Label(root,text="length of the password:",font=('ariel',15,'bold'),fg="black") 
Entry1 = Entry(root)
Entry2 = Entry(root,text="")
l1.pack()
Entry1.pack()
Entry2.pack(pady=20)
  
f1=Frame(root)
f1.pack(pady=20)
b1 = Button (f1 , text="generate"  , command =  password,width=15, height=1)

b1.grid(row=10,column=20,pady=20)
root.mainloop()

    