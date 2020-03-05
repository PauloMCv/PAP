import tkinter as tk
from tkinter import ttk, messagebox
import datetime, time



hoje = datetime.date.today()

main=tk.Tk()
StatusBar = tk.LabelFrame(main, relief="sunken",bd=1)
StatusBar.grid(row=3,column=0,columnspan=3,sticky="WES",pady=(20,0))

welcomeMsg = 'Cv Corporation - Funcionário: Paulo Carvalho'
statusBar = tk.Label(StatusBar)
statusBar.grid(row=0,column=0)

def relogio():
    def tit_tac(welcomeMsg):
        data = "{:02d}/{:02d}/{:4d}".format(hoje.day,
                                            hoje.month,
                                            hoje.year)
        # Vai Buscar as horas do computador
        tempo = time.strftime('%H:%M:%S')
        #Atualiza a Label do statusbard
        statusBar.config(text=welcomeMsg+" "*232+data+", "+tempo)
        #Chama a função a si mesma a cada 200 milisegunos
        #para atualizar o tempo que for preciso
        statusBar.after(200, relogio)

    tit_tac(welcomeMsg)

relogio()

main.mainloop()
