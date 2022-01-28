from tkinter import *
from random import choice

app = Tk()
app.title('Random Number Chooser')
app.geometry('350x100')
inp = Entry(app)
inp.grid(row=0, column=0, columnspan=2)


def pick():
    i = (inp.get()).split(',')
    msg = Label(app, text=choice(i))
    msg.grid(row=2, column=0)


B = Button(app, text='Choose', command=pick)
B.grid(row=1, column=0)

quitB = Button(app, text='cancel', command=app.quit)
quitB.grid(row=1, column=1)
app.mainloop()
