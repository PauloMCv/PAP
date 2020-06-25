import database as db
import tkinter as tk
import datetime, time
from tkinter import ttk
from tkinter import ttk, messagebox
from tkinter import *
import admin


def login():
    def ver_login(user_var,password_var):
        username = user_var.get()
        password = password_var.get()
        logado = db.validar(username,password)
        if logado == "owner":
            rank = "Dono"
        elif logado == "admin":
            rank = "Admin"
        elif logado == "guess":
            rank = "Empregado"
        else:
            rank = "erro"
            messagebox.showerror(title='Error',message='Username ou password incorretos')
        if rank != "erro":
            if rank == "Dono":
                w1.destroy()
                w.destroy()
                admin.main(username)
            elif rank == "Admin":
                w1.destroy()
                w.destroy()
                admin.main(username)
            else:
                w1.destroy()
                w.destroy()
                admin.main(username)

    def sair():
        resp=messagebox.askyesno('Sair do Programa','Deseja realmente sair do programa ?')
        if resp == True:
            messagebox.showinfo('Sair do Programa','Até uma proxima')
            w1.destroy()
            w.destroy()

    w = tk.Tk()
    w.iconbitmap('img/logos/favicon.ico')
    w_width = 480
    w_height = 425
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
    #Labels , Entrys e butões

    logo_img=tk.PhotoImage(file='img/logos/logo_64.png')
    logo=tk.Label(w,image=logo_img)
    logo.pack(pady=10)

    bem_vindo=tk.Label(w,text="Bem-Vindo \n Por favor introduza os dados abaixo",foreground="blue",font=("Helvetica", 20))
    bem_vindo.pack()

    user_label=tk.Label(w,text="Username",foreground="black",font=("Helvetica", 16))
    user_label.pack()
    user_var = tk.StringVar()
    user_entry = tk.Entry(w,width=30,borderwidth=3,textvariable=user_var)
    user_entry.pack(ipady=3)
    user_entry.focus()

    password_label=tk.Label(w,text="Password",foreground="black",font=("Helvetica", 16))
    password_label.pack()
    password_var = tk.StringVar()
    password_entry = tk.Entry(w,width=30,borderwidth=3,show="•",textvariable=password_var)
    password_entry.pack(ipady=3)

    login_button=tk.Button(w,text="Login",width=10,foreground="white",background="blue",font=("Helvetica", 15),command=lambda:ver_login(user_var,password_var))
    login_button.place(x=70,y=350)

    leave_button=tk.Button(w,text="Sair",width=10,foreground="white",background="red",font=("Helvetica", 15),command=sair)
    leave_button.place(x=300,y=350)
    ###############################################################################
    w.mainloop()

login()
