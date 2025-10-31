import tkinter as tk
from tkinter import messagebox, simpledialog
import datetime
import time
import threading
import os
import json
import subprocess

# Caminhos
BASE_DIR = os.path.expanduser("~/alarme")
CONFIG_FILE = os.path.join(BASE_DIR, "horarios.json")
SOM = os.path.join(BASE_DIR, "sino.mp3")
IMAGEM = os.path.join(BASE_DIR, "alarme.png")

# Carregar horários salvos
def carregar_horarios():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return []

# Salvar horários
def salvar_horarios():
    with open(CONFIG_FILE, "w") as f:
        json.dump(horarios, f)

# Função que toca o alarme
def tocar_alarme():
    subprocess.Popen(["feh", "--fullscreen", IMAGEM])
    subprocess.run(["cvlc", "--play-and-exit", SOM])
    time.sleep(10)
    os.system("pkill feh")

# Monitor de horários
def monitorar_horarios():
    while True:
        agora = datetime.datetime.now().strftime("%H:%M")
        if agora in horarios:
            tocar_alarme()
            time.sleep(60)  # Evita repetir no mesmo minuto
        time.sleep(1)

# Funções da interface
def adicionar_horario():
    novo = simpledialog.askstring("Novo horário", "Digite o horário (HH:MM):")
    if novo:
        if len(novo) == 5 and novo[2] == ":":
            horarios.append(novo)
            horarios.sort()
            salvar_horarios()
            atualizar_lista()
        else:
            messagebox.showerror("Erro", "Formato inválido. Use HH:MM")

def remover_horario():
    selecionado = lista.curselection()
    if selecionado:
        horario = lista.get(selecionado)
        horarios.remove(horario)
        salvar_horarios()
        atualizar_lista()
    else:
        messagebox.showinfo("Aviso", "Selecione um horário para remover.")

def atualizar_lista():
    lista.delete(0, tk.END)
    for h in horarios:
        lista.insert(tk.END, h)

# Janela principal
root = tk.Tk()
root.title("Alarme Escolar")
root.geometry("300x400")

tk.Label(root, text="Horários de Alarme", font=("Arial", 14, "bold")).pack(pady=10)

lista = tk.Listbox(root, font=("Arial", 12))
lista.pack(pady=5, fill=tk.BOTH, expand=True)

tk.Button(root, text="Adicionar horário", command=adicionar_horario).pack(pady=5)
tk.Button(root, text="Remover selecionado", command=remover_horario).pack(pady=5)

tk.Label(root, text="O programa deve ficar aberto para funcionar.", font=("Arial", 9)).pack(pady=10)

# Iniciar
horarios = carregar_horarios()
atualizar_lista()

# Thread de monitoramento
thread = threading.Thread(target=monitorar_horarios, daemon=True)
thread.start()

root.mainloop()
