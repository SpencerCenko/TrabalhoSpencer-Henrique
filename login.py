import string
import tkinter as tk #importando a tela
from tkinter import messagebox, LabelFrame, PhotoImage#são as funções que estou puxando da biblioteca do tkinter
import mysql.connector
"""
Login: usuario senha: 1234
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



tk.Label(janela, text="Usuário").place(x=50,y=20) #Onde ira aparecer uma mensagem

nome = tk.Entry(janela)
nome.place(height=20,width=150,x=100,y=20)# campo de texto onde iremos digitar o nome

tk.Label(janela, text="Senha").place(x=50,y=70)#Onde ira aparecer uma mensagem
senha = tk.Entry(janela, show="*")# campo de texto onde iremos digitar a senha
senha.place(height=20,width=150,y=70,x=100)


def log():
    e1 = nome.get()#passando o valor do label para uma varialvel par dar print no nome
    e2 =senha.get()#passando o valor do label para uma varialvel par dar print na senha 
     
    query = "select nome from log where nome = '"+e1+"'"#funções sendo passadas para o mysql e sendo definidas dentro de uma variavel
    query2 = "select senha from log where nome = '"+e1+"'"#funções sendo passadas para o mysql e sendo definidas dentro de uma variavel
    cursor.execute(query, e1)#usa o cursor para executar o comando e a variavel mais o e1 que e == nome.get()
    userNome = str(cursor.fetchone()).replace("(", "").replace(")", "").replace("]", "").replace("[", "").replace("'", "").replace(",", "")#ele subistitui os caracteres por caracteres vazios e o str trasforma o cursor.fetchone() em string pois ele vem como truple
    cursor.execute(query2, e1)#usa o cursor para executar o comando e a variavel mais o e2 que e == senha.get()
    userSenha = str(cursor.fetchone()).replace("(", "").replace("(", "").replace(")", "").replace("]", "").replace("[", "").replace("'", "").replace(",", "")#ele subistitui os caracteres por caracteres vazios e o str trasforma o cursor.fetchone() em string pois ele vem como truple 
    if(e1 == ""and e2 == ""):
     messagebox.showerror("Erro",'Digite os valores')#messagebox importado par quando os dados estiverm em branco

    if(e1 == userNome and e2 == userSenha): 
        tk.Label(janela,text="Login efetuado com sucesso").place(x=100,y=200)
        janela.destroy()#fecha a janela principal 
        jsecundaria = tk.Tk()#definindo a janela 
        jsecundaria.title("Principal")#Nome da janela 
        jsecundaria.config(bg="#b5b5b5")
        jsecundaria.geometry("400x250")#tamanho da janela
        jsecundaria.resizable(0,0)#não permite que a janela seja maximizada
        tk.Label(jsecundaria,text='ID:',bg="#b5b5b5").place(x=10,y=10,)#X e de um lado pro outro e y cima e baixo
        tk.Label(jsecundaria,text='Nome:',bg="#b5b5b5").place(x=9,y=45)#X e de um lado pro outro e y cima e baixo
        tk.Label(jsecundaria,text='Preço:',bg="#b5b5b5").place(x=9,y=80)#X e de um lado pro outro e y cima e baixo

        id=tk.Entry(jsecundaria)
        nome2=tk.Entry(jsecundaria)
        preco=tk.Entry(jsecundaria)
        preco.place(width=150,x=50,y=80)
        nome2.place(width=150,x=50,y=45)
        id.place(width=150,x=35,y=10)


        tk.Button(jsecundaria,text='select').place(x=10,y=130)#botao de select
        tk.Button(jsecundaria,text='update').place(x=60,y=130)#botao de update 
        tk.Button(jsecundaria,text='insert').place(x=120,y=130)#botao de insert
        tk.Button(jsecundaria,text='delet').place(x=170,y=130)#botao de delet
    else:
        tk.Label(janela,text="nome/senha estao incorretos").place(x=100,y=200)#mostra quando os dados do usuarios estão incorretos
        
botao = tk.Button(janela, text="Entrar",command=log).place(height=50,width=100,y=100,x=50)#botao que executa a ação
janela.bind('<Return>',lambda event:log())#Return e no nome do enter no teclado lambda event manda a função pedida

janela.mainloop()
