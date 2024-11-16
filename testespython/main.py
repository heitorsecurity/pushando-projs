import tkinter as tk
import sqlite3

def cadastrar_pessoa():
    nome = entry_nome.get()
    email = entry_email.get()

    conn = sqlite3.connect('cadastros.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pessoas (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

    lista_cadastros.insert(tk.END, f"{nome} - {email} ✅")  # Emoji de confirmação

# ... (código para criar a janela, os campos de entrada, o botão e a lista de cadastros)
