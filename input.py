from tkinter import *
from random import choice, sample

app = Tk()
app.title('App')
app.geometry('250x100')
inp = Entry(app, background='white', borderwidth=5, relief='groove')
app['background'] = 'grey'
ch = IntVar()
s = Scale(app, from_=0, to=5, variable=ch, orient=HORIZONTAL)
s.grid(row=1, columnspan=2, column=0, padx=25, pady=5)

inp.grid(row=0, column=0, columnspan=4, pady=10)


def show():
    i = (inp.get()).split(' ')
    if ch.get() != 1:
        ele = sample(i, ch.get())
        bl = ''
        for e in ele:
            bl += ' ' + e
        cho = 'Choice: ' + str(bl)
    else:
        cho = 'Choice: ' + str(choice(i))
    out = Toplevel()
    out.title('Choice')

    msg = Label(out, text=cho, relief='sunken', width=25)
    msg.grid(row=3, column=1, columnspan=2)
    if c['state'] == DISABLED:
        c['state'] = NORMAL


b = Button(app, text='Click', command=show, borderwidth=5, relief='groove')
c = Button(app, text='Clear', command=app.quit, state=DISABLED, borderwidth=5, relief='raised')

c.grid(row=2, column=0, padx=25, pady=5)
b.grid(row=2, column=1, padx=25, pady=5)
app.mainloop()
