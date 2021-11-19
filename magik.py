from tkinter import *
import random

root=Tk()

root.title("Lucky Friend")
root.geometry("500x500")
root.configure(background = 'lavender')

zlist = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Ava', 'Lucas', 'Charlotte']
print(zlist)

def rn():
    random_no = random.randint(0,7)
    print(random_no)
    thatonefriend = zlist[random_no]
    print("Your Lucky friend is: " + thatonefriend)
    
zmagicalbutton = Button(root, text="Show your lucky friend, totally not scuffed", command = rn)
zmagicalbutton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()