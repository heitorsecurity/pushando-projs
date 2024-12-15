import time

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime

class MinhaGUI:
    def __init__(self):
        self.janela_principal = Tk() # Criar janela
        self.janela_principal.title('Relógio by heitorsecurity')
        # Criado botão e empacotar botao janela
        self.botao = Button(self.janela_principal, text='Iniciar', command=self.hello_world)
        self.botao.pack()
        # Criado botao do relogio e empacotar
        self.lbl = Label(self.janela_principal, font=('calibri', 120, 'bold'),
                         background='black', foreground='white')
        self.lbl.pack(anchor='center')
        self.time() # Iniciar relogio
        self.janela_principal.mainloop() # Rodar a janela principal

    # Função para exibir o tempo com milissegundos
    def time(self):
        now = datetime.now() # Obtém o horário atual
        string = now.strftime('%H:%M:%S') + f".{now.microsecond // 1000:03d}" # Formata com milissegundos
        self.lbl.config(text=string) # Atualiza o texto do rótulo
        self.lbl.after(1, self.time) # Atualiza a cada 1 milissegundo

    def hello_world(self):
        messagebox.showinfo('Oi', 'Voce clicou o botão!')

gui = MinhaGUI() # Iniciar a GUI

#    Exemplo de como integrar no Tkinter
#    root = Tk()
#    root.title()
#    mainloop() # Rodando