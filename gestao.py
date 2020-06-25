import database as db
import tkinter as tk
import datetime, time
from tkinter import ttk
from tkinter import ttk, messagebox
from tkinter import *

def dono(username):
    def relogio():
        def tit_tac(welcomeMsg):
            data = "{:02d}/{:02d}/{:4d}".format(hoje.day,
                                                hoje.month,
                                                hoje.year)
            # Vai Buscar as horas do computador
            tempo = time.strftime('%H:%M:%S')
            #Atualiza a Label do statusbard
            statusBar.config(text=welcomeMsg+" "*35+data+", "+tempo+" "*20)
            #Chama a função a si mesma a cada 200 milisegunos *
            #*para atualizar o tempo que for preciso
            statusBar.after(200, relogio)
        tit_tac(welcomeMsg)

    hoje = datetime.date.today()

    username=db.info(username)
    p_nome=db.infopnome(username)
    u_nome=db.infounome(username)
    rank=db.inforank(username)

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
    #Fundo
    w1=tk.Toplevel(w)
    w1.wm_attributes('-fullscreen','1')
    bgimage = tk.PhotoImage(file='img/logos/fundo.png')
    background_label = tk.Label(w1,width=2000,height=2000,image=bgimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    bem_vindo=tk.Label(w,text="Painel de Dono ",foreground="blue",font=("Helvetica", 20))
    bem_vindo.place(x=180,y=0)

    StatusBar = tk.LabelFrame(w, relief="sunken",bd=1)
    StatusBar.place(x=0,y=425)
    welcomeMsg = 'Cv Corporation - Store Management | Username: '+ username
    statusBar = tk.Label(StatusBar)
    statusBar.grid(row=0,column=0)
    relogio()
    w.mainloop()


def gerente(username):
    def relogio():
        def tit_tac(welcomeMsg):
            data = "{:02d}/{:02d}/{:4d}".format(hoje.day,
                                                hoje.month,
                                                hoje.year)
            # Vai Buscar as horas do computador
            tempo = time.strftime('%H:%M:%S')
            #Atualiza a Label do statusbard
            statusBar.config(text=welcomeMsg+" "*35+data+", "+tempo+" "*20)
            #Chama a função a si mesma a cada 200 milisegunos *
            #*para atualizar o tempo que for preciso
            statusBar.after(200, relogio)
        tit_tac(welcomeMsg)

    hoje = datetime.date.today()

    username=db.info(username)
    p_nome=db.infopnome(username)
    u_nome=db.infounome(username)
    rank=db.inforank(username)

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
    #Fundo
    w1=tk.Toplevel(w)
    w1.wm_attributes('-fullscreen','1')
    bgimage = tk.PhotoImage(file='img/logos/fundo.png')
    background_label = tk.Label(w1,width=2000,height=2000,image=bgimage)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    bem_vindo=tk.Label(w,text="Painel de Gerente ",foreground="blue",font=("Helvetica", 20))
    bem_vindo.place(x=180,y=0)

    StatusBar = tk.LabelFrame(w, relief="sunken",bd=1)
    StatusBar.place(x=0,y=425)
    welcomeMsg = 'Cv Corporation - Store Management | Username: '+ username
    statusBar = tk.Label(StatusBar)
    statusBar.grid(row=0,column=0)
    relogio()
    w.mainloop()
Admin = 'Admin'
dono(Admin)
