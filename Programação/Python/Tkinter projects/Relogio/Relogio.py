######  importanto As bibliotecas necessarias #######

from tkinter import * ##### Importanto tudo do Tkinter ########
from datetime import datetime ###### Importando biblioteca de datas e tempo ######### 
import pyglet #### Importando biblioteca para improtar fontes personalizadas ######

###### Criando Variáveis #######

pyglet.font.add_file("digital-7.ttf")# importantdo arquivo da fonte#
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul
fundo = cor1
cor = cor2

###### Iniciando tela grafica com Tkinter ########
janela = Tk() # chamando toda a biblioteca e suas funções para uma variavel #
janela.resizable(False , False) # informando que a janela irá er um tamanho fixo #
janela.title("")# definindo um titulo vazio para a janela #
janela.geometry("400x160")# Definindo resolução do programa#
janela.configure(bg=fundo)# configurando A cor de fundo com a funcao "bg"#

##### Criando função que ira armazenar todos os valores necessarios ####
def relogio():
    tempo = datetime.now()### defininfo a variavel "tempo" , e atribuindo o valor da função geral datetime###
    hora = tempo.strftime("%H:%M:%S")### definindo a variavel "hora" e dessa vez atribuindo valores da hora , minutos e segundos#####
    dia_semana = tempo.strftime("%A")### definindo a variavel "dia_semana" e dando a ela o valor apenas do dia da semana , por extenso####
    dia_numero  =tempo.day### definindo a variavel "dia_numero" e atribuindo valor do dia da semana , porém com um valor inteiro ou seja , um numero ####
    mes = tempo.strftime("%b")### definindo a variavel "mes" e dando valor da função de tempo , porem apenas o valor do mes ####
    ano = tempo.strftime("%y")### definindo a variavel "ano" e dando valor igual ao ano atual###


    ### após Criar os campos gráficos###
    Hora.config(text=hora)### definindo configuração da label "Hora" que criamos para alterar o seu texto e incorporar o valor da varialvel "hora"###
    Hora.after(200 , relogio)### Para deixar o relogio dinamico e nao estácio , precisamos fazer com que ele se atualize a cada 200 milisegudos###
    Data.config(text=dia_semana+"     "+str(dia_numero) + "/" + str(mes)+ "/" + str(ano))
    


Hora = Label(janela , text="" , font=("digital-7 80") , bg=fundo , fg=cor6)
Hora.grid(row=0 , column=0 , sticky=NW , padx=60)

Data = Label(janela , text="" , font=("digital-7 20 ") , bg=fundo  , fg=cor)
Data.grid(row=1 , column=0 ,  sticky=NW , padx=80)


relogio()
janela.mainloop()
