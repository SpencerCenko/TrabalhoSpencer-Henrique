import string
import tkinter as tk #importando a tela
from tkinter import messagebox, LabelFrame

      
janela = tk.Tk() #definindo o nome da tela

janela.title("Login")
janela.geometry('400x300') #definido o tamanho da tela 
tk.Label(janela, text="Usuário").pack(pady=10) #Onde ira aparecer uma mensagem
nome = tk.Entry(janela)# campo de texto onde iremos digitar o nome
nome.pack(pady=10)
tk.Label(janela, text="Senha").pack(pady=10)#Onde ira aparecer uma mensagem
senha = tk.Entry(janela, show="*")# campo de texto onde iremos digitar a senha
senha.pack(pady=10)
def log():
    e1 = nome.get()#passando o valor do label para uma varialvel par dar print no nome
    e2 =senha.get()#passando o valor do label para uma varialvel par dar print na senha 
    if(e1 == 'carro' and e2 == '123'):
        jsecundaria = tk.Tk()#definindo a janela 
        jsecundaria.title("Principal")#Nome da janela
        jsecundaria.geometry("400x250")#tamanho da janela
    else:
        tk.Label(janela,text="nome/senha estao incorretos").pack(padx=10)
botao = tk.Button(janela, text="Entrar",command=log).pack(padx=10)#botao que executa a ação
   

janela.mainloop()
it works!
good!
