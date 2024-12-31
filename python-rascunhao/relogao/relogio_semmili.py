import time

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Relógio by heitorsecurity')

def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1, time)

#milli_sec = int(round(time.time() * 1000))

lbl = Label(root, font=('calibri', 120, 'bold'),
            background='black',
            foreground='white')

lbl.pack(anchor='center')
time()

mainloop()
""" Descartar esse ou usar? """
