from tkinter import *

app = Tk()
ch = StringVar()
menu = OptionMenu(app,ch,'Red','Blue','Black','White')
menu.pack()
app.mainloop()