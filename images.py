from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

app = Tk()
app.title('App')


def show():

    app.name = filedialog.askopenfilename(initialdir='res', title='Select an Image', filetypes=(
        ('PNG Images', '*.png'),))
    b.destroy()
    img = ImageTk.PhotoImage(Image.open(app.name))
    lbl = Label(app, image=img)
    lbl.pack()


b = Button(app, text='View', command=show)
b.pack()
app.mainloop()
