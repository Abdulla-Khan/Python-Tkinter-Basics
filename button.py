from tkinter import *
from random import randint
app = Tk()
app.title('App')
app.geometry('250x100')


def show():
    msg = Label(app, text=randint(1,100))
    msg.pack()


b = Button(app, text='Click', command=show)
b.pack()
app.mainloop()
