from tkinter import *

app = Tk()
choice = StringVar()
rb = Radiobutton(app, text='RB1 Selected', value='RB1 Selected', variable=choice)
rb1 = Radiobutton(app, text='RB2 Selected', value='RB2 Selected', variable=choice)
rb.deselect()
rb1.deselect()
rb.pack()
rb1.pack()


def show():
    msg = Label(app, text=choice.get())
    msg.pack()


b = Button(app, command=show, text='Show')
b.pack()
app.mainloop()
