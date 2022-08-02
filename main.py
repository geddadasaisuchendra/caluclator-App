from tkinter import *

root = Tk()
root.title("sai caluclator")
e = Entry(root, width=50, borderwidth=20, fg='blue')
e.grid(row=0, column=0, columnspan=20, padx=20, pady=30)


#declaring functtions
def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def buttonadd():
    firstnum = e.get()
    e.delete(0, END)
    global fnum
    global math
    math = "add"
    fnum = int(firstnum)
    e.delete(0, END)


def equal():
    secondnum = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0, fnum + int(secondnum))
    elif math == "sub":
        e.insert(0, fnum - int(secondnum))
    elif math == "mul":
        e.insert(0, fnum * int(secondnum))
    elif math == "div":
        e.insert(0, fnum / int(secondnum))


#oprations
def sub():
    firstnum = e.get()
    e.delete(0, END)
    global fnum
    global math
    math = "sub"
    fnum = int(firstnum)
    e.delete(0, END)
    return


def mul():
    firstnum = e.get()
    e.delete(0, END)
    global fnum
    global math
    math = "mul"
    fnum = int(firstnum)
    e.delete(0, END)
    return


def div():
    firstnum = e.get()
    e.delete(0, END)
    global fnum
    global math
    math = "div"
    fnum = int(firstnum)
    e.delete(0, END)
    return


#buttons
button1 = Button(root, text="1", padx=40, pady=20,
                 command=lambda: click(1)).grid(row=3, column=0)
button2 = Button(root, text='2', padx=40, pady=20,
                 command=lambda: click(2)).grid(row=3, column=1)
button3 = Button(root, text="3", padx=40, pady=20,
                 command=lambda: click(3)).grid(row=3, column=2)
button4 = Button(root, text="4", padx=40, pady=20,
                 command=lambda: click(4)).grid(row=2, column=0)
button5 = Button(root, text="5", padx=40, pady=20,
                 command=lambda: click(5)).grid(row=2, column=1)
button6 = Button(root, text="6", padx=40, pady=20,
                 command=lambda: click(6)).grid(row=2, column=2)
button7 = Button(root, text="7", padx=40, pady=20,
                 command=lambda: click(7)).grid(row=1, column=0)
button8 = Button(root, text="8", padx=40, pady=20,
                 command=lambda: click(8)).grid(row=1, column=1)
button9 = Button(root, text="9", padx=40, pady=20,
                 command=lambda: click(9)).grid(row=1, column=2)
button0 = Button(root, text="0", padx=40, pady=20,
                 command=lambda: click(0)).grid(row=4, column=0)

#operations
buttonadd = Button(root, text="+", padx=40, pady=20, command=buttonadd).grid(row=4,column=1)
buttonsub = Button(root, text="-", padx=40, pady=20, command=sub).grid(row=4,column=2)
buttonmul = Button(root, text="*", padx=40, pady=20, command=mul).grid(row=5,column=0)
buttondiv = Button(root, text="/", padx=40, pady=20, command=div).grid(row=5,column=1)
buttonequal = Button(root, text="=", padx=40, pady=20, command=equal).grid(row=5,column=2)
buttonclear = Button(root, text="clear", padx=40, pady=20, command=clear).grid(row=6,column=0)
buttonexit = Button(root, text="exit", padx=40, pady=20, command=root.quit).grid(row=6,column=1)
root.mainloop()
