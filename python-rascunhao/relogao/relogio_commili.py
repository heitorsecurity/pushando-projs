import time

from tkinter import *
from tkinter.ttk import *
from datetime import datetime

# Função exibir tempo em milissegundos
def time():
    now = datetime.now() # Puxa horário atual
    string = now.strftime('%H:%M:%S') + f".{now.microsecond // 1000:03d}" # Formata em milissegundos
    lbl.config(text=string) # Atualiza o texto
    lbl.after(1, time) # Atualiza por 1 milissegundo

# Integrar no Tkinter
root = Tk()
root.title('Relógio by heitorsecurity')
lbl = Label(root, font=('calibri', 120, 'bold'),
            background='black',
            foreground='white')
lbl.pack(anchor='center')
time()
mainloop()
