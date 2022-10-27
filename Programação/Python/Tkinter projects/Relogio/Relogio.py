
from tkinter import *
from datetime import datetime
import pyglet

pyglet.font.add_file("digital-7.ttf")
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul
fundo = cor1
cor = cor2


janela = Tk()
janela.resizable(False, False)
janela.title("")
janela.geometry("400x160")
janela.configure(bg=fundo)


def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia_numero = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%y")

    Hora.config(text=hora)
    Hora.after(200, relogio)
    Data.config(text=dia_semana+"     "+str(dia_numero) +
                "/" + str(mes) + "/" + str(ano))


Hora = Label(janela, text="", font=("digital-7 80"), bg=fundo, fg=cor6)
Hora.grid(row=0, column=0, sticky=NW, padx=60)

Data = Label(janela, text="", font=("digital-7 20 "), bg=fundo, fg=cor)
Data.grid(row=1, column=0,  sticky=NW, padx=80)


relogio()
janela.mainloop()
