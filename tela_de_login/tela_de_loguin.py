from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores

cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters

#criando janela

janela = Tk()
janela.title("Login")
janela.geometry("310x300")
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

# dados para logar

Dados = ["william", "123"]

def verificação_senha():
    nome = caixa_de_texto_nome.get()
    senha = caixa_de_texto_senha.get()

    if Dados[0] == nome and Dados[1] == senha:
        messagebox.showinfo("Login", "Seja bem vindo " + Dados[0])

        #apagar o que estiver no freme cima e baixo 
       
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
    else:
        messagebox.showwarning("Erro","Verifique o nome e Senha!")

#criando a janela após o loguin 

def nova_janela():
    #frame cima 
    nome_usuário = Label(frame_cima,text= "Usuário: " + Dados[0], anchor=NE,font=("Ivy 20"),bg=cor1, fg=cor4)
    nome_usuário.place(x=5, y=5)

    linha_nome_usuário = Label(frame_cima,text= "",width=200, anchor=NE,font=("Ivy 25"),bg=cor2, fg=cor4)
    linha_nome_usuário.place(x=5, y=45)
    
    #frame baixo

    mensagem = Label(frame_baixo,text= "Bem vindo ao sistema "+ Dados[0], anchor=NE,font=("Ivy 17"),bg=cor1, fg=cor4)
    mensagem.place(x=5, y=105)

#dividindo a janela

frame_cima=Frame(janela,width=310, height=50,bg=cor1,relief="flat")
frame_cima.grid(row=0, column =0,pady=1,padx=0,sticky=NSEW)

frame_baixo=Frame(janela,width=310, height=250,bg=cor1,relief="flat")
frame_baixo.grid(row=1, column =0,pady=1,padx=0,sticky=NSEW)

# configurando frame de cima  

login = Label(frame_cima,text= "Loguin", anchor=NE,font=("Ivy 25"),bg=cor1, fg=cor4)
login.place(x=5, y=5)

linha_login = Label(frame_cima,text= "",width=200, anchor=NE,font=("Ivy 25"),bg=cor2, fg=cor4)
linha_login.place(x=5, y=45)

# configurando frame baixo

nomelabel = Label(frame_baixo,text="Nome*", anchor=NW,font=("Arial 10"),bg=cor1, fg=cor4)
nomelabel.place(x=5, y=20)
caixa_de_texto_nome = Entry(frame_baixo, width=25, justify="left", font=("Arial", 15), highlightthickness=1, relief="solid")
caixa_de_texto_nome.place(x=5,y=50)

senhalabel = Label(frame_baixo,text="Senha*", anchor=NW,font=("Arial 10"),bg=cor1, fg=cor4)
senhalabel.place(x=5, y=100)
caixa_de_texto_senha = Entry(frame_baixo, width=25, justify="left",show="*", font=("Arial", 15), highlightthickness=1, relief="solid")
caixa_de_texto_senha.place(x=5,y=130)

botão_confirma = Button(frame_baixo,text= "Entrar",command=verificação_senha,width= 39, height=2,font=("Arial 8 bold"),bg=cor2, fg=cor1,relief=RAISED, overrelief=RIDGE)
botão_confirma.place(x=5, y=180)

janela.mainloop()