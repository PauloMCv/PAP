#Modulos que Vão ser Usados
import tkinter as tk
from tkinter import ttk
from tkinter import *
#import hora
#import database as db

#######################################################################
#1 Variaveis
MAX_LABELS=9
LABELS_LINHA=3
#1 FIM
#######################################################################
#2 Funções
def entrar_evento(obj):
    obj.config()

def sair_evento(obj):
    obj.config()

def entrar(obj):
    obj.bind('<Enter>',lambda event:entrar_evento(obj))

def sair(obj):
    obj.bind('<Leave>',lambda event:sair_evento(obj))

def clicar_evento(obj):
    print(obj['text'])
    obj['fg']='red'

def clicar(obj):
    obj.bind('<Button-1>',lambda event:clicar_evento(obj))
#2 FIM
#######################################################################
#3 Configurações da Janela
w = tk.Tk()

#3 FIM
#######################################################################
#4 Imports de Imagens, etc...

#4 FIM
#######################################################################
#5 Notebook
note = ttk.Notebook(w)

tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)

note.add(tab1, text = "Tab One")
note.add(tab2, text = "Tab Two")
note.add(tab3, text = "Tab Three")
note.grid()
#5 FIM
#######################################################################
#6 Criação dos Botões nos Notebooks
teste=tk.PhotoImage(file ="./img/pastel.png")
bot_label=[]
for i in range(MAX_LABELS):
    aux=tk.Label(tab1,text=str(i),image=teste)
    bot_label.append(aux)
    bot_label[i].grid(row=i//LABELS_LINHA,column=i%LABELS_LINHA)
    entrar(bot_label[i])
    sair(bot_label[i])
    clicar(bot_label[i])
#6 FIM
#######################################################################
#7 Outro Código



#7 FIM
#######################################################################
w.mainloop()
