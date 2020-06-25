import database as db
import tkinter as tk
import datetime, time
from tkinter import ttk
from tkinter import ttk, messagebox
from tkinter import *
import gestao as painel
import client as menu
#import client

#def main(nome_verificar):

    #username=db.info(nome_verificar)
username = "gerente"
p_nome=db.infopnome(username)
u_nome=db.infounome(username)
rank=db.inforank(username)

def relogio():
    def tit_tac(welcomeMsg):
        data = "{:02d}/{:02d}/{:4d}".format(hoje.day,
                                            hoje.month,
                                            hoje.year)
        # Vai Buscar as horas do computador
        tempo = time.strftime('%H:%M:%S')
        #Atualiza a Label do statusbard
        statusBar.config(text=welcomeMsg+" "*81+data+", "+tempo)
        #Chama a função a si mesma a cada 200 milisegunos *
        #*para atualizar o tempo que for preciso
        statusBar.after(200, relogio)
    tit_tac(welcomeMsg)

def gestao():
    if rank == "owner":
        w1.destroy()
        w.destroy()
        painel.dono(username)
    if rank == "admin":
        w1.destroy()
        w.destroy()
        painel.gerente(username)

def venda():
    w1.destroy()
    w.destroy()
    menu.venda()

def sair():
    resp=messagebox.askyesno('Sair do Programa','Deseja realmente sair do programa ?')
    if resp == True:
        messagebox.showinfo('Sair do Programa','Até uma proxima')
        w1.destroy()
        w.destroy()

hoje = datetime.date.today()

w = tk.Tk()
w.iconbitmap('img/logos/favicon.ico')
w_width = 550
w_height = 450
screen_w = w.winfo_screenwidth()
screen_h = w.winfo_screenheight()
w_x = (screen_w/2) - (w_width/2)
w_y = (screen_h/2) - (w_height/2)
w.geometry('%dx%d+%d+%d' % (w_width,w_height,w_x,w_y))
w.resizable(0,0)
w.overrideredirect(True)
w.wm_attributes("-topmost",1)


###############################################################################
#Fundo
w1=tk.Toplevel(w)
w1.wm_attributes('-fullscreen','1')
bgimage = tk.PhotoImage(file='img/logos/fundo.png')
background_label = tk.Label(w1,width=2000,height=2000,image=bgimage)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
###############################################################################
#Labels Entrys Buttons , etc.

bem_vindo=tk.Label(w,text="Bem - Vindo \n Escolha uma das opções abaixo",foreground="blue",font=("Helvetica", 20))
bem_vindo.place(x=70,y=0)

admin_button=tk.Button(w,text="Menu de Gestão",width=15,foreground="white",background="blue",font=("Helvetica", 15),command=gestao)
admin_button.place(x=30,y=150)

venda_button=tk.Button(w,text="Menu de Venda",width=15,foreground="white",background="blue",font=("Helvetica", 15),command=venda)
venda_button.place(x=340,y=150)

venda_button=tk.Button(w,text="Sair",width=15,foreground="white",background="red",font=("Helvetica", 15),command=sair)
venda_button.place(x=180,y=300)

###############################################################################
#Horas Com Mensagem

StatusBar = tk.LabelFrame(w, relief="sunken",bd=1)
StatusBar.place(x=0,y=425)

welcomeMsg = 'Cv Corporation - Store Management'
statusBar = tk.Label(StatusBar)
statusBar.grid(row=0,column=0)

relogio()
###############################################################################
w.mainloop()
