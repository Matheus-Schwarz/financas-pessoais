from datetime import date
from datetime import timedelta
from tkinter import Frame
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import END


class DataEntry(Frame):
    def __init__(self, pai):
        super().__init__(master=pai)
        bot1 = Button(self, text='-', command=self.diminui_data)
        bot1.grid(row=0, column=0)
        self.campo_dia = Entry(self, width=3)
        self.campo_dia.grid(row=0, column=1)
        lbl1 = Label(self, text='/')
        lbl1.grid(row=0, column=2)
        self.campo_mes = Entry(self, width=3)
        self.campo_mes.grid(row=0, column=3)
        lbl2 = Label(self, text='/')
        lbl2.grid(row=0, column=4)
        self.campo_ano = Entry(self, width=6)
        self.campo_ano.grid(row=0, column=5)
        bot2 = Button(self, text='+', command=self.aumenta_data)
        bot2.grid(row=0, column=6)

    def aumenta_data(self):
        dia = int(self.campo_dia.get())
        mes = int(self.campo_mes.get())
        ano = int(self.campo_ano.get())
        data = date(ano, mes, dia)
        data += timedelta(1)
        self.campo_dia.delete(0, END)
        self.campo_dia.insert(0, data.day)
        self.campo_mes.delete(0, END)
        self.campo_mes.insert(0, data.month)
        self.campo_ano.delete(0, END)
        self.campo_ano.insert(0, data.year)

    def diminui_data(self):
        dia = int(self.campo_dia.get())
        mes = int(self.campo_mes.get())
        ano = int(self.campo_ano.get())
        data = date(ano, mes, dia)
        data += timedelta(-1)
        self.campo_dia.delete(0, END)
        self.campo_dia.insert(0, data.day)
        self.campo_mes.delete(0, END)
        self.campo_mes.insert(0, data.month)
        self.campo_ano.delete(0, END)
        self.campo_ano.insert(0, data.year)

    def pega_data(self):
        try:
            dia = int(self.campo_dia.get())
        except:
            dia = date.today().day
        try:
            mes = int(self.campo_mes.get())
        except:
            mes = date.today().month
        try:
            ano = int(self.campo_ano.get())
        except:
            ano = date.today().year
        return date(ano, mes, dia)

    def pega_data_formatada(self):
        data = self.pega_data()
        dia = data.day
        mes = data.month
        ano = data.year
        if dia < 10:
            dia = f"0{dia}"
        else:
            dia = str(dia)
        if mes < 10:
            mes = f"0{mes}"
        else:
            mes = str(mes)
        return dia + '/' + mes + '/' + str(ano)

    def default(self):
        data = date.today()
        self.campo_dia.delete(0, END)
        self.campo_dia.insert(0, data.day)
        self.campo_mes.delete(0, END)
        self.campo_mes.insert(0, data.month)
        self.campo_ano.delete(0, END)
        self.campo_ano.insert(0, data.year)

    def insere_data(self, data):
        self.campo_dia.delete(0, END)
        self.campo_dia.insert(0, data.day)
        self.campo_mes.delete(0, END)
        self.campo_mes.insert(0, data.month)
        self.campo_ano.delete(0, END)
        self.campo_ano.insert(0, data.year)


class ListEntry(Frame):
    lista = []
    indice = -1

    def __init__(self, pai, lista, tamanho):
        super().__init__(master=pai)
        self.lista = lista
        bot1 = Button(self, text='-', command=self.diminui_indice)
        bot1.grid(row=0, column=0)
        self.campo_indice = Entry(self, width=tamanho)
        self.campo_indice.grid(row=0, column=1)
        bot2 = Button(self, text='+', command=self.aumenta_indice)
        bot2.grid(row=0, column=2)

    def diminui_indice(self):
        self.indice = self.pega_indice()
        if self.indice > -1:
            self.indice -= 1
            self.campo_indice.delete(0, END)
            if self.indice > -1:
                self.campo_indice.insert(0, self.lista[self.indice])

    def aumenta_indice(self):
        self.indice = self.pega_indice()
        if self.indice < len(self.lista)-1:
            self.indice += 1
            self.campo_indice.delete(0, END)
            self.campo_indice.insert(0, self.lista[self.indice])

    def pega_indice(self):
        contador = 0
        procurado = self.campo_indice.get()
        for elemento in self.lista:
            if elemento == procurado:
                return contador
            contador += 1
        return self.indice


class IndiceEntry(Frame):
    indice = 0
    limite = 0

    def __init__(self, pai, limite, tamanho=4):
        super().__init__(master=pai)
        self.limite = limite
        bot1 = Button(self, text='-', command=self.diminui_indice)
        bot1.grid(row=0, column=0)
        self.campo_indice = Entry(self, width=tamanho)
        self.campo_indice.grid(row=0, column=1)
        bot2 = Button(self, text='+', command=self.aumenta_indice)
        bot2.grid(row=0, column=2)

    def diminui_indice(self):
        self.pega_indice()
        if self.indice > -1:
            self.indice -= 1
            self.campo_indice.delete(0, END)
            if self.indice > 0:
                self.campo_indice.insert(0, self.indice)

    def aumenta_indice(self):
        self.pega_indice()
        if self.indice < self.limite:
            self.indice += 1
            self.campo_indice.delete(0, END)
            self.campo_indice.insert(0, self.indice)

    def pega_indice(self):
        try:
            self.indice = int(self.campo_indice.get())
        except:
            self.indice = 0

    def retorna_indice(self):
        try:
            return int(self.campo_indice.get())
        except:
            return 0
