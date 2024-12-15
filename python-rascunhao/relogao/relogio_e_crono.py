#import time

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime

class MinhaGUI:
    def __init__(self):
        self.janela_principal = Tk() # Criar janela
        self.janela_principal.title('Relógio by heitorsecurity')
        # Criado botão e empacotar botao janela
        self.botao_croini = Button(self.janela_principal, text='Cronometro Iniciar', command=self.hello_world)
        self.botao_croparar = Button(self.janela_principal, text='Cronometro Parar', command=self.hello_world)
        self.botao_relogio = Button(self.janela_principal, text='Mostra relógio', command=self.hello_world)
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit)
        self.botao_croini.pack(side="bottom")
        self.botao_croparar.pack(side="bottom")
        self.botao_relogio.pack(side="bottom")
        self.botao_sair.pack(side="bottom")
        # Criado botao do relogio e empacotar
        self.lbl = Label(self.janela_principal, font=('calibri', 120, 'bold'),
                         background='white', foreground='black')
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