from tkinter import *

app = Tk()
app.title('CheckBox')
ch = StringVar()
chk = Checkbutton(app, text='CheckBox', variable=ch, onvalue='Yes', offvalue='Nope')
chk.deselect()
chk.pack()


def show():
    msg = Label(app, text=ch.get())
    msg.pack()


b = Button(app, command=show, text='Show')
b.pack()
app.mainloop()
