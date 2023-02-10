from tkinter import *
from tkinter import ttk
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

azul_fundo = "#1e3743"
corborda = "#759fe6"
corfundoframe = "#dfe3ee"
corbotão = "#187db2"
root = Tk()

class Relatórios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def gerarRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        #criando corpo do relatório
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50,700, 'Código: ')
        self.c.drawString(50,680, 'Nome: ')
        self.c.drawString(50, 660, 'Telefone: ')
        self.c.drawString(50, 640, 'Cidade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(125, 700, self.codigoRel)
        self.c.drawString(125, 680,self.nomeRel)
        self.c.drawString(132,660,self.telefoneRel)
        self.c.drawString(125,640, self.cidadeRel)

        self.c.rect(20 ,635 , 550, 80 , fill=False, stroke=True)


        self.c.showPage()
        self.c.save()
        self.printCliente()


class Funcs():
    def limpa_tela(self):#limpa os campos de cadastro de cliente
        self.codigo_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self): #criando a função para o banco de dados
        self.conn =sqlite3.connect("clientes.bd")#conectando o banco de dados e criando o banco de dados com nome
        self.cursor = self.conn.cursor()
    def desconectar_bd(self): # desconectando banco de dados
        self.conn.close() ; print("Desconectando banco de dados" )
    def montaTabelas(self):#montando as tabelas para armazenar os dados
        self.conecta_bd(); print("Conectando ao banco de dados")
        ### Criar tabela
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(cod INTEGER PRIMARY KEY, nome_cliente CHAR(40) NOT NULL, telefone INTEGER(20), cidade CHAR (40));""")
        self.conn.commit(); print("BANCO DE DADOS CRIADO")#criando a tabela com colunas
        self.desconectar_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO clientes(nome_cliente, telefone,cidade)VALUES(?, ?, ?)""",(self.nome, self.telefone,self.cidade))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listacli.delete(*self.listacli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod,nome_cliente,telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listacli.insert("", END,values=i)
        self.desconectar_bd()
    def ondoubleclick(self, event):
        self.limpa_tela()
        self.listacli.selection()

        for n in self.listacli.selection():
            col1, col2, col3, col4, =self.listacli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self, cod=None):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()

        self.desconectar_bd()
        self.limpa_tela()
        self.select_lista()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ? , cidade = ? WHERE cod = ?""",(self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconectar_bd()
        self.select_lista()
        self.limpa_tela()




class Application(Funcs,Relatórios): #definindo a classe do aplicativo para rodar
    def __init__(self):
        self.root = root #nomear root antes de fazer os códigos
        self.tela() #para rodar a definição tela (rodar a configuração dentro do def)
        self.frames_da_tela() #colocando a função dos frames para rodar no app
        self.widgetsframe1() #colocando widgets do frame 1 para rodar no sistema
        self.lista_frame2() #colocando a lista do frame 2 para rodar no sistema
        self.menus()  # colocando o menu para rodar no sistema
        self.montaTabelas()#colocando as tabelas para rodar no sistema
        self.select_lista()#colocando a lista para rodar no sistema com o banco de c=dados embutido
        root.mainloop() #para fazer o app rodar
    def tela(self): # configurações do aplicativo
        self.root.title("Cadastro de clientes") #titulo da janela
        self.root.configure(background=azul_fundo) #cor
        self.root.geometry("700x500") # tamanh da tela inicial
        self.root.resizable(True,True)#tela responsiva a tamanho pode ser aumentado
        self.root.maxsize(width=900 , height= 700) #colocando limite de tamanho maximo da janela
        self.root.minsize(width=500 , height=400) #colocando limite minimo da janela
    def frames_da_tela(self): #criando a classe de frames para a tela
        self.frame_1 = Frame(self.root,bd=4,bg=corfundoframe,highlightbackground=corborda,highlightthickness=2) #criando o frame 1 com borda
        self.frame_1.place(relx=0.02 , rely=0.02 , relwidth=0.96 , relheight=0.46 )#relx e rely usa a porcentagem para posicionamento, relwidth porcentagem da largura e relheigth porcentagem da altura.

        self.frame_2 = Frame(self.root,bd=4,bg=corfundoframe,highlightbackground=corborda,highlightthickness=2)
        self.frame_2.place(relx=0.02 , rely=0.50 , relwidth=0.96 , relheight=0.46 )   #para o frame 2 foi alterado apenas o posicionamento em y
    def widgetsframe1(self): #criando os botões bd= borda bg= cor do botão  fg= cor das letras font= configurações de fonte 1 fonte, tamanho,negrito.
        self.bt_limpar = Button(self.frame_1, text= "LIMPAR", bd=2 , bg=corbotão, fg="white", font=("verdana", 7,"bold"), command= self.limpa_tela)  #CRIANDO BOTÕES E COLOCANDO O NOME
        self.bt_limpar.place(relx=0.2, rely=0.1 , relwidth= 0.1 , relheight= 0.15 ) #CRIANDO A POSIÇÃO E TAMANHO DO BOTÃO
        self.bt_buscar = Button(self.frame_1, text="BUSCAR", bd=2 , bg=corbotão, fg="white", font=("verdana", 7,"bold"))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo = Button(self.frame_1, text="NOVO", bd=2 , bg=corbotão, fg="white", font=("verdana", 7,"bold"),command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar = Button(self.frame_1, text="ALTERAR", bd=2 , bg=corbotão, fg="white", font=("verdana", 7,"bold"), command= self.altera_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar = Button(self.frame_1, text="APAGAR", bd=2 , bg=corbotão, fg="white", font=("verdana", 7,"bold"),command=self.deleta_cliente)

        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        #criando a label e entrada do código
        self.lb_codigo = Label(self.frame_1,text="Código",bg=corfundoframe) #criando a label
        self.lb_codigo.place(relx= 0.05, rely=0.05) #posicionando a label
        self.codigo_entry = Entry(self.frame_1) #criando o entry
        self.codigo_entry.place(relx=0.05 , rely=0.15 , relwidth=0.08) # posicionando o entry
        # criando a label e entrada do nome do cliente
        self.lb_nome = Label(self.frame_1, text="Nome",bg=corfundoframe)
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.6)
        # criando a label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone",bg=corfundoframe)
        self.lb_telefone.place(relx=0.05, rely=0.60)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.40)
        # criando a label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade",bg=corfundoframe)
        self.lb_cidade.place(relx=0.5, rely=0.6)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.40)
    def lista_frame2(self): #criando a lista de clientes no frame 2
        self.listacli = ttk.Treeview(self.frame_2, height= 3, column=("col1","col2","col3","col4"))
        self.listacli.heading("#0" , text="") #colocando os cabeçalhos das colunas
        self.listacli.heading("#1", text="Código")
        self.listacli.heading("#2", text="Nome")
        self.listacli.heading("#3", text="Telefone")
        self.listacli.heading("#4", text="Cidade")

        #colocando o tamanho das colunas
    #o tamanho da coluna é dividida em 500 onde 50 seria 10% da tela
        self.listacli.column("#0", width=1)
        self.listacli.column("#1", width=50)
        self.listacli.column("#2", width=200)
        self.listacli.column("#3", width=125)
        self.listacli.column("#4", width=125)

        self.listacli.place(relx=0.01, rely=0.1 , relwidth=0.95, relheight=0.85)

        self.scrollista = Scrollbar(self.frame_2, orient="vertical")
        self.listacli.configure(yscroll=self.scrollista.set)
        self.scrollista.place(relx=0.96 , rely=0.1,relwidth=0.04, relheight=0.85)

        self.listacli.bind("<Double-1>", self.ondoubleclick)
    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu= menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)


        def Quit(): self.root.destroy()
        menubar.add_cascade(label="opções", menu= filemenu)
        menubar.add_cascade(label="Sobre", menu= filemenu2)

        filemenu.add_command(label="sair",command=Quit)
        filemenu.add_command(label="Limpa Tela", command= self.limpa_tela)
        filemenu.add_command(label="Ficha do Cliente", command=self.gerarRelatCliente)



Application()
