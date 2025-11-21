import string
import tkinter as tk #importando a tela
from tkinter import messagebox, LabelFrame, PhotoImage#são as funções que estou puxando da biblioteca do tkinter
import mysql.connector
"""
quando for usar comandos de insert,update e delet
query = "insert into log (nome,senha)values(%s,%s)"
cursor.execute(query,(nome.get(),senha.get()))
conexao.commit()

query = "update log set nome=%s,senha=%s where id = 43"
cursor.execute(query,(nome.get(),senha.get())
conexao.commit()

cursor.execute("delete from log where id=15")    
conexao.commit()
"""
conexao = mysql.connector.connect(host='localhost',database='login',user='root',password='')#conector do python com o mysql


cursor = conexao.cursor()#o objeto que usamos para mexer no mysql pelo pyhon

janela = tk.Tk() #definindo o nome da tela
icon = PhotoImage(file="logoPy.png") #definindo uma imagem como icone
janela.iconphoto(False, icon) #definindo icon como icone da janela
janela.title("Login")#nome da janela
janela.resizable(0,0)#desabilita a função de maximizar a tela de login
janela.geometry('400x300') #definido o tamanho da tela 


conexao.commit()#e obrigatio o uso quando for usar comandos de insert,update e delet ele que manda as alterações do codigo
tk.Label(janela, text="Usuário").pack(pady=10) #Onde ira aparecer uma mensagem
nome = tk.Entry(janela)# campo de texto onde iremos digitar o nome
nome.pack(pady=10)
tk.Label(janela, text="Senha").pack(pady=10)#Onde ira aparecer uma mensagem
senha = tk.Entry(janela, show="*")# campo de texto onde iremos digitar a senha
senha.pack(pady=10)


def log():
    e1 = nome.get()#passando o valor do label para uma varialvel par dar print no nome
    e2 =senha.get()#passando o valor do label para uma varialvel par dar print na senha 
    query = "select nome from log where nome = '"+e1+"'"
    query2 = "select senha from log where nome = '"+e1+"'"
    cursor.execute(query, e1)
    userNome = str(cursor.fetchone()).replace("(", "").replace(")", "").replace("]", "").replace("[", "").replace("'", "").replace(",", "")
    cursor.execute(query2, e1)
    userSenha = str(cursor.fetchone()).replace("(", "").replace("(", "").replace(")", "").replace("]", "").replace("[", "").replace("'", "").replace(",", "")
     if(e1 == ""and e2 == ""):
     messagebox.showerror("Erro",'Digite os valores')
    
    if(e1 == userNome and e2 == userSenha): 
        tk.Label(janela,text="Login efetuado com sucesso").pack(padx=10)
    else:
        tk.Label(janela,text="nome/senha estao incorretos").pack(padx=10)#mostra quando os dados do usuarios estão incorretos
        
        
        
       
botao = tk.Button(janela, text="Entrar",command=log).pack(padx=10)#botao que executa a ação

janela.mainloop()
'''
 cursor.execute("select * from log")#comando para o banco
        dados = cursor.fetchall()#pega todas os dados do banco
        jsecundaria = tk.Tk()#definindo a janela 
        
        jsecundaria.title("Principal")#Nome da janela 
        jsecundaria.geometry("400x250")#tamanho da janela
        tk.Label(jsecundaria,text=dados+"\n").pack() 
    else:
        tk.Label(janela,text="nome/senha estao incorretos").pack(padx=10)#mostra quando os dados do usuarios estão incorretos
'''
