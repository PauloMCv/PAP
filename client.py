import tkinter as tk
from tkinter import ttk
from tkinter import *
import database as db

#def venda():


######################
#Algumas Variaveis
MAX_LABELS=15
LABELS_LINHA=6
######################
#CORES
dark = "#3b3d3c"
verde = "#d2ffd2"
vermelho = "#dd0202"
########################
#Funções e Classes
def altf4_sair():
    w1.destroy()
    w.destroy()

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

##########################################################
#Janelas
w = tk.Tk()
w.config(bg=dark)
#w.geometry('1920x1800')
w.wm_attributes('-fullscreen','1')
w.resizable(0,0)
#########
w1=tk.Toplevel(w)
w1.wm_attributes("-topmost",1)
w1.overrideredirect(True)
x = w.winfo_x()
y = w.winfo_y()
w1.geometry("+%d+%d" %(x+900,y+200))
w1.protocol("WM_DELETE_WINDOW",altf4_sair)
##############################################################################################################
#Styles
style = ttk.Style()
style.theme_create( "notebook", parent="classic", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0],"background": dark }},
        "TFrame": {"configure": {"background": "white"}},
        "TNotebook.Tab": {"configure": {"padding": [20, 10], "background": verde, "font":("Helvetica", 15)},
        "map": {"background": [("selected", "white")]}}})
style.theme_use("notebook")
##############################################################################################################
#Notebook
note = ttk.Notebook(w,width=800,height=600,padding=10)
#TABS
tab1 = ttk.Frame(note)
tab2 = ttk.Frame(note)
tab3 = ttk.Frame(note)
tab4 = ttk.Frame(note)
tab5 = ttk.Frame(note)
tab6 = ttk.Frame(note)
tab7 = ttk.Frame(note)
tab8 = ttk.Frame(note)
note.add(tab1, text = "Geral") #Sem categoria
note.add(tab2, text = "Bolos") #Categoria A
note.add(tab3, text = "Salgados") #Categoria B
note.add(tab4, text = "Bebidas") #Categoria C
note.add(tab5, text = "Doces") #Categoria D
note.add(tab6, text = "Gelados") #Categoria E
note.add(tab7, text = "Menus") #Categoria M
note.add(tab8, text = "Outros") #Categoria N
note.place(x=0,y=0)

bot_label=[]
#imagens = tk.PhotoImage(file = './img/menu'+str(i)+'.png')
#imagens = tk.PhotoImage(file = './img/produtos/a_pastel.png')
img_url = './img/produtos/'
categoria="a"
produto="pastel"
imagem = tk.PhotoImage(file = img_url+categoria+"_"+produto+".png")
for i in range(MAX_LABELS):
    aux=tk.Label(tab1,text=str(i),image=imagem)#image=imagens
    bot_label.append(aux)
    bot_label[i].grid(row=i//LABELS_LINHA,column=i%LABELS_LINHA,pady=10,padx=10)
    entrar(bot_label[i])
    sair(bot_label[i])
    clicar(bot_label[i])

if True:
    pass
w.mainloop()

'''
bot_label2=[]
for i in range(MAX_LABELS):
    aux=tk.Label(tab2,text=str(i),image=imagens)
    bot_label2.append(aux)
    bot_label2[i].grid(row=i//LABELS_LINHA,column=i%LABELS_LINHA,pady=10,padx=10)
    entrar(bot_label2[i])
    sair(bot_label2[i])
    clicar(bot_label2[i])
'''
