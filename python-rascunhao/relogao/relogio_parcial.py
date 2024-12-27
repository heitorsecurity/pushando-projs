import time

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from datetime import datetime

class MinhaGUI:
    def __init__(self):
        self.janela_principal = Tk() # Criar janela
        self.janela_principal.title('Relógio by heitorsecurity')
        # Variaveis de tempo
        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Criado botão e empacotar botao janela
        self.botao_croini = Button(self.janela_principal, text='Cronometro Iniciar', command=self.start_timer)
        self.botao_croparar = Button(self.janela_principal, text='Cronometro Parar', command=self.stop_timer)
        self.botao_relogio = Button(self.janela_principal, text='Mostra relógio', command=self.hello_world)
        self.botao_sair = Button(self.janela_principal, text='Sair', command=self.janela_principal.quit)
        self.botao_croini.pack(side="bottom")
        self.botao_croparar.pack(side="bottom")
        self.botao_relogio.pack(side="bottom")
        self.botao_sair.pack(side="bottom")

        # Criar uma label para o display de timer
        self.timer_label = Label(self.janela_principal, font=('calibri', 120, 'bold'), text="00:00:00.000")
        self.timer_label.pack()

        # Criado botao do relogio e empacotar
        self.lbl = Label(self.janela_principal, font=('calibri', 120, 'bold'), background='white', foreground='black')
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

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            self.elapsed_time = time.time() - self.start_time
            hours, rem = divmod(self.elapsed_time, 3600)
            minutes, seconds = divmod(rem, 60)
            miliseconds = int((rem % 1) * 1000)
            time_str = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{miliseconds:03}"
            self.timer_label.config(text=time_str)
            self.timer_label.after(10, self.update_timer) # Atualiza a cada 10 milisegundos

gui = MinhaGUI() # Iniciar a GUI

#    Exemplo de como integrar no Tkinter
#    root = Tk()
#    root.title()
#    mainloop() # Rodando