from tkinter import *
#gui interaction
window = Tk()
window.geometry("500x500")
window.configure(bg="black")
window.title("Basic Calculator")
#entry to box
e = Entry(window,width = 80,borderwidth = 5,font = ("Times New Roman",50))
e.grid(row = 0, column = 0, padx = 10, pady = 10)
frame1 = Frame(window,bg = "Black")

e.grid(row = 0, column = 0, padx = 10, pady = 10)
e.place(x = 0,y = 0,height = 150)
frame1.pack()

#buttons
def click(nums):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result) + str(nums))
button = Button(window,text = "1",width = 12, command = lambda:click(1))
button.place(x = 50,y = 170,height = 50)
button = Button(window,text = "2",width = 12,command = lambda:click(2))
button.place(x = 150,y = 170,height = 50)
button = Button(window,text = "3",width = 12,command = lambda:click(3))
button.place(x = 250,y = 170,height = 50)
button = Button(window,text = "4",width = 12,command = lambda:click(4))
button.place(x = 350,y = 170,height = 50)
button = Button(window,text = "5",width = 12,command = lambda:click(5))
button.place(x = 50,y = 250,height = 50)
button = Button(window,text = "6",width = 12,command = lambda:click(6))
button.place(x = 150,y = 250,height = 50)
button = Button(window,text = "7",width = 12,command = lambda:click(7))
button.place(x = 250,y = 250,height = 50)
button = Button(window,text = "8",width = 12,command = lambda:click(8))
button.place(x = 350,y = 250,height = 50)
button = Button(window,text = "9",width = 12,command = lambda:click(9))
button.place(x = 50,y = 330,height = 50)
button = Button(window,text = "0",width = 12,command = lambda:click(0))

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)

button.place(x = 150,y = 330,height = 50)
button = Button(window,text = "+",width = 12,command = add)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0,END)

button.place(x = 50,y = 410,height = 50)
button = Button(window,text = "-",width = 12,command = sub)
button.place(x = 150,y = 410,height = 50)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)
button = Button(window,text = "*",width = 12,command = mult)
button.place(x = 250,y = 410,height = 50)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)

button = Button(window,text = "/",width = 12,command = div)
button.place(x = 350,y = 410,height = 50)

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math ==  "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i*int(n2))
    elif math == "division":
        e.insert(0,i/int(n2))

button = Button(window,text = "=",width = 12,command = equal)
button.place(x = 350,y = 330,height = 50)

def clear():
    e.delete(0,END)
button = Button(window,text = "CLEAR",width = 12,command = clear)
button.place(x = 250,y = 330,height = 50)

mainloop()