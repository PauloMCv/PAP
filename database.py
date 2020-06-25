import sqlite3
import hashlib

def criar_bd():
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    d_sql='CREATE TABLE IF NOT EXISTS Contas(username TEXT,password TEXT,pnome TEXT,unome TEXT,ordenado REAL,rank TEXT)'
    d_sql1='CREATE TABLE IF NOT EXISTS Produtos(nome TEXT,preco REAL,preco_fabricante REAL,stock INTEGER,categoria TEXT,designacao TEXT)'
    d_sql2='CREATE TABLE IF NOT EXISTS Dinheiro(atual REAL,gasto REAL)'
    cursor.execute(d_sql)
    cursor.execute(d_sql1)
    cursor.execute(d_sql2)
    conn.commit()
    conn.close()

criar_bd()

#####################################################################################################
#Login, Registar e Apagar
def validar(username,password):
    conn = sqlite3.connect('database.sqlite3')
    logado = False
    password2 = password
    password_enc = hashlib.sha256(password2.encode()).hexdigest()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contas")
    rows = cursor.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPass = row[1]
        dbRank = row[5]
        if dbUser == username and dbPass == password_enc:
            if dbRank == "owner":
                logado = "owner"
            elif dbRank == "admin":
                logado = "admin"
            elif dbRank == "guess":
                logado = "guess"
            else:
                logado = "erro"
            return logado
            conn.commit()
            conn.close()
            break

def registar(username_reg,password_reg,pnome_reg,unome_reg,ordenado_reg,rank_reg):
    pws = password_reg
    password = hashlib.sha256(pws.encode()).hexdigest()
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Contas (username,password,pnome,unome,ordenado,rank) VALUES (?,?,?,?,?,?)", (username_reg,password,pnome_reg,unome_reg,ordenado_reg,rank_reg))
    conn.commit()
    conn.close()

def deletar(username_del):
    conn = sqlite3.connect('database.sqlite3')
    cursor=conn.cursor()
    d_sql = 'DELETE FROM Contas WHERE username=?'
    cursor.execute(d_sql,(username_del,))
    conn.commit()
    conn.close()
#####################################################################################################
#Info e Usernames

def usernames(lista_usernames):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    d_sql = 'SELECT username FROM Contas'
    cursor.execute(d_sql)
    linhas = cursor.fetchall()
    conn.close()
    for username in linhas:
        lista_usernames.append(username[0])

def info(username):
    return username

def infopnome(username):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contas")
    rows = cursor.fetchall()
    for row in rows:
        dbUser = row[0]
        dbPnome = row[2]
        if dbUser == username:
            return dbPnome
            conn.commit()
            conn.close()
            break

def infounome(username):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contas")
    rows = cursor.fetchall()
    for row in rows:
        dbUser = row[0]
        dbUnome = row[3]
        if dbUser == username:
            return dbUnome
            conn.commit()
            conn.close()
            break

def inforank(username):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Contas")
    rows = cursor.fetchall()
    for row in rows:
        dbUser = row[0]
        dbRank = row[5]
        if dbUser == username:
            return dbRank
            conn.commit()
            conn.close()
            break
##################################################################################################################################################################
#Listar

def listar_nomes(lista_nomes):
    conn = sqlite3.connect('database.sqlite3')
    cur=conn.cursor()
    d_sql = 'SELECT nome FROM Cargos'
    cur.execute(d_sql)
    linhas=cur.fetchall()
    conn.close()
    for nome in linhas:
        lista_nomes.append(nome[0])

def listar_cargo(lista_cargos):
    conn = sqlite3.connect('database.sqlite3')
    cur=conn.cursor()
    d_sql = 'SELECT cargo FROM Cargos'
    cur.execute(d_sql)
    linhas=cur.fetchall()
    conn.close()
    for cargo in linhas:
        lista_cargos.append(cargo[0])
##################################################################################################################################################################
#Alterar
def adicionar(nome_reg,cargo_reg):
    conn = sqlite3.connect('database.sqlite3')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Cargos (nome,cargo) VALUES (?,?)", (nome_reg,cargo_reg))
    conn.commit()
    conn.close()

def remover(nome_del):
    conn = sqlite3.connect('database.sqlite3')
    cursor=conn.cursor()
    d_sql = 'DELETE FROM Cargos WHERE nome=?'
    cursor.execute(d_sql,(nome_del,))
    conn.commit()
    conn.close()
