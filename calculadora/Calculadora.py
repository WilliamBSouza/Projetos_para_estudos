#passo 1 - criar e importar as bibliotecas necessárias para o projeto

#vamos importar o tkinter

from tkinter import *
from tkinter import ttk

#cor
cor1 = "#0c0c0d" #preto
cor2 = "#f5f5f7" #branco
cor3 = "#0505eb" #azul
cor4 = "#c1c1c9" #cinzenta
cor5 = "#e39b14" #laranja

#passo 2 - crie a janela e fazer as configurações básicas

janela = Tk()
janela.title("Calculadora")
janela.geometry("278x330")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=280, height=70, bg=cor3)

frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=280, height=330)
frame_corpo.grid(row=1, column=0)

#variavel todos valores

todos_valores = ""

#criando a label

valor_texto = StringVar()

#criando função

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)


    #passando para o visor

    valor_texto.set(todos_valores)

#função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))

    #função limpar a tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#criando label (visor)

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=9, relief=FLAT, anchor="e",justify=RIGHT,font=('Ivy 21'),bg=cor3,fg=cor2)
app_label.place(x=0,y=0)

#criando botões


b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=12,height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo,command = lambda: entrar_valores("%") , text="%", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_2.place(x=135,y=0)
b_3 = Button(frame_corpo,command = lambda: entrar_valores("/") ,  text="/", width=6, height=2, bg= cor5,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_3.place(x=207,y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores("7") ,  text="7", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_4.place(x=0,y=52)
b_5 = Button(frame_corpo,command = lambda: entrar_valores("8") , text="8", width=6, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_5.place(x=69,y=52)
b_6 = Button(frame_corpo,command = lambda: entrar_valores("9") ,  text="9", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_6.place(x=137,y=52)
b_7 = Button(frame_corpo,command = lambda: entrar_valores("*") , text="*", width=6, height=2, bg= cor5,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_7.place(x=207,y=52)

b_8 = Button(frame_corpo, command = lambda: entrar_valores("4") , text="4", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_8.place(x=0,y=104)
b_9 = Button(frame_corpo,command = lambda: entrar_valores("5") , text="5", width=6, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_9.place(x=69,y=104)
b_10 = Button(frame_corpo,command = lambda: entrar_valores("6") ,  text="6", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_10.place(x=137,y=104)
b_11 = Button(frame_corpo,command = lambda: entrar_valores("-") , text="-", width=6, height=2, bg= cor5,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_11.place(x=207,y=104)

b_12 = Button(frame_corpo,command = lambda: entrar_valores("1") ,  text="1", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_12.place(x=0,y=156)
b_13 = Button(frame_corpo,command = lambda: entrar_valores("2") , text="2", width=6, height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_13.place(x=69,y=156)
b_14 = Button(frame_corpo, command = lambda: entrar_valores("3") , text="3", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_14.place(x=137,y=156)
b_15 = Button(frame_corpo,command = lambda: entrar_valores("+") , text="+", width=6, height=2, bg= cor5,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_15.place(x=207,y=156)

b_16 = Button(frame_corpo,command = lambda: entrar_valores("0") ,  text="0", width=12,height=2, bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo,command = lambda: entrar_valores(".") ,  text=".", width=6,height=2,bg= cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_17.place(x=135,y=208)
b_18 = Button(frame_corpo, command = calcular , text="=", width=6, height=2, bg= cor5,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
b_18.place(x=207,y=208)


janela.mainloop()

