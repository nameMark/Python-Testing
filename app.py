#prve

from tkinter import *

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="keep me sign in")
c.grid(columnspan=2)
root.mainloop()


#druhe


from tkinter import *

root = Tk()


def printName(Event):
    print("ahoj ja sa volam Marko")


button_1 = Button(root, text="print moje meno")
button_1.bind("<Button-1>", printName)
button_1.pack()
root.mainloop()

#tretie


from tkinter import *

root = Tk()


def leftClick(event):
    print("left")


def middleClick(event):
    print("middle")


def rightClick(event):
    print("right")


frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-3>", middleClick)
frame.bind("<Button-2>", rightClick)
frame.pack()


root.mainloop()

#  stvrte

from tkinter import *

def doNothing():
    print("ok ok lel")

root = Tk()
# main menu
menu = Menu(root)
root.config(menu=menu)

podMenu = Menu(menu)
menu.add_cascade(label="File", menu=podMenu )
podMenu.add_command(label="novy projekt", command = doNothing)
podMenu.add_command(label="nove", command = doNothing)
podMenu.add_separator()
podMenu.add_command(label="exit", command = doNothing)

editMenu= Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="redo ctrl + z", command = doNothing)

# tool bar
toolbar = Frame(root, bg="blue")

instertButt = Button(toolbar, text="Insert image ", command= doNothing)
instertButt.pack(side=LEFT, padx= 10, pady=10)
printButt = Button(toolbar, text="Print  ", command= doNothing)
printButt.pack(side=LEFT, padx= 10, pady=10)

toolbar.pack(side=TOP, fill = X)

# status bar

status = Label (root, text="robenie nicoho", bd= 10, relief= SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()


#piate 

from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Okno", "ako sa mas ? ")

answer = tkinter.messagebox.askquestion("otazka", "mas  ma rad ?")

if answer ==  "yes":
    print ("  :-----/   ")
elif  answer == "no":
    print (":-)")
root.mainloop()


#sieste 

from tkinter import *

root = Tk()

canvas = Canvas (root, width = 200, height= 100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50)
redLine = canvas.create_line(0,100, 200, 50, fill="red")
greenBox = canvas.create_rectangle(25, 25, 130,60, fill="purple")

canvas.delete(redLine)
canvas.delete(ALL)

root.mainloop()

