from tkinter import *

app = Tk()
ch = IntVar()
s = Scale(app,from_= 0,to=100,variable=ch,orient=HORIZONTAL)
s.pack()
def show():
    msg = Label(app, text=ch.get())
    msg.pack()


b = Button(app, command=show, text='Show')
b.pack()
app.mainloop()