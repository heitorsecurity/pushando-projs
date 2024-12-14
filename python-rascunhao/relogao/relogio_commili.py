import time

from tkinter import *
from tkinter.ttk import *
from datetime import datetime

# Função para exibir o tempo com milissegundos
def time():
    now = datetime.now() # Obtém o horário atual
    string = now.strftime('%H:%M:%S') + f".{now.microsecond // 1000:03d}" # Formata com milissegundos
    lbl.config(text=string) # Atualiza o texto do rótulo
    lbl.after(1, time) # Atualiza a cada 1 milissegundo

# Exemplo de como integrar no Tkinter
root = Tk()
root.title('Relógio by heitorsecurity')
lbl = Label(root, font=('calibri', 120, 'bold'),
            background='black',
            foreground='white')
lbl.pack(anchor='center')
time()
mainloop()
