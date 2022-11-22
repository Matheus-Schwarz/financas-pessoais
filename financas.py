from tkinter import Tk
from tkinter import Frame
from tkinter import Button

from financeiro.vsv import GestorVSV
from financeiro.vsv import FrameDadosVSV
from financeiro.vsv import FrameFiltrosVSV

from financeiro.mywidgets import IndiceEntry
from financeiro.mywidgets import ListEntry


meubanco = GestorVSV()
meubanco.nome_banco = 'financas.txt'
meubanco.regua = ['indice', 'texto', 'tags', 'texto', 'texto', 'valor', 'data']
meubanco.filtros = [[None, None], None, None, None, None, [None, None], [None, None]]
meubanco.cabecalho = '|ID|DESCRICAO|TAGS|FONTE|DESTINO|VALOR|DATA|'
meubanco.edita_cabecalho(0, 2)
meubanco.edita_cabecalho(1, 20)
meubanco.edita_cabecalho(2, 20)
meubanco.edita_cabecalho(3, 15)
meubanco.edita_cabecalho(4, 13)
meubanco.edita_cabecalho(5, 8)
meubanco.edita_cabecalho(6, 6)


janela = Tk()
janela.title('PROGRAMA DE FINANCAS')
janela.geometry('540x200')

cont_coluna1 = Frame(janela)
cont_coluna1.grid(row=0, column=0)

cont_dados = FrameDadosVSV(cont_coluna1, meubanco.regua, meubanco.pega_titulos()[1:])
cont_dados.grid(row=0, column=0)

cont_indice = Frame(cont_coluna1)
cont_indice.grid(row=1, column=0)

def insere_indice():
    dados = cont_dados.pega_dados()
    meubanco.insere_dados(dados)
    campo_indice.limite = meubanco.pega_indice()

bot_insere = Button(cont_indice, text='INSERE', command=insere_indice, width=13)
bot_insere.grid(row=0, column=0)

def deleta_indice():
    campo_indice.pega_indice()
    indice = campo_indice.indice
    if indice > 0:
        meubanco.deleta_dados(indice)
    campo_indice.limite = meubanco.pega_indice()

bot_deleta = Button(cont_indice, text='DELETA', command=deleta_indice, width=13)
bot_deleta.grid(row=1, column=0)

cont_pesquisa_indice = Frame(cont_indice)
cont_pesquisa_indice.grid(row=0, column=1)
campo_indice = IndiceEntry(cont_pesquisa_indice, meubanco.pega_indice(), 6)
campo_indice.grid(row=0, column=0)

def pesquisa_indice():
    campo_indice.pega_indice()
    indice = campo_indice.indice
    if indice > 0:
        dados = meubanco.pesquisa_dados(indice)
        cont_dados.insere_dados(dados[1:])

bot_pesquisa = Button(cont_pesquisa_indice, text='X', command=pesquisa_indice, width=2)
bot_pesquisa.grid(row=0, column=1)

def atualiza_indice():
    campo_indice.pega_indice()
    indice = campo_indice.indice
    if indice > 0:
        dados = cont_dados.pega_dados()
        meubanco.edita_dados(indice, dados)

bot_atualiza = Button(cont_indice, text='ATUALIZA', command=atualiza_indice, width=13)
bot_atualiza.grid(row=1, column=1)

cont_coluna2 = Frame(janela)
cont_coluna2.grid(row=0, column=1)

cont_filtros = FrameFiltrosVSV(cont_coluna2, meubanco.regua, meubanco.pega_titulos())
cont_filtros.grid(row=0, column=0)


def exibir_relatorio():
    meubanco.filtros = cont_filtros.pega_filtros()
    meubanco.mostra_dados()

cont_coluna3 = Frame(janela)
cont_coluna3.grid(row=0, column=2)
bot_mostra = Button(cont_coluna3, command=exibir_relatorio, text='EXIBIR RELATORIO')
bot_mostra.grid(row=0, column=0)
campo_ordem = ListEntry(cont_coluna3, meubanco.pega_titulos(), 12)
campo_ordem.grid(row=1, column=0)

def organizar():
    indice = campo_ordem.pega_indice()
    if indice > -1:
        meubanco.organiza_dados(indice)

bot_organiza = Button(cont_coluna3, command=organizar, text='ORGANIZAR')
bot_organiza.grid(row=2, column=0)

def saldos_p():
    meubanco.filtros = cont_filtros.pega_filtros()
    meubanco.gera_saldos(completo=False)

def saldos_c():
    meubanco.gera_saldos()

bot_saldos_parc = Button(cont_coluna3, command=saldos_p, text='EXIBIR SALDOS PARC')
bot_saldos_parc.grid(row=3, column=0)

bot_saldos_comp = Button(cont_coluna3, command=saldos_c, text='EXIBIR SALDOS COMP')
bot_saldos_comp.grid(row=4, column=0)

janela.mainloop()




