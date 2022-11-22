from datetime import date
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import END
from financeiro.mywidgets import DataEntry


class GestorVSV:
    nome_banco = ''
    regua = ['indice']
    filtros = [[None, None]]
    cabecalho = '| ID |'

    def cria_banco(self):
        banco = open(self.nome_banco, 'w')
        banco.close()
        print(self.nome_banco)
        self.cria_backup()

    def cria_backup(self):
        banco = open(self.nome_banco[:-4] + '_backup.txt', 'w')
        banco.close()

    def insere_coluna(self, posicao, tipo, nome, valor_incial):
        self.regua.insert(posicao, tipo)
        self.filtros.insert(posicao, None)
        novo_cabecalho = self.cabecalho[1:-1].split('|')
        if tipo == 'data':
            novo_cabecalho.insert(posicao, f'   {nome}   ')
        else:
            novo_cabecalho.insert(posicao, nome)
        self.cabecalho = '|'
        for item in novo_cabecalho:
            self.cabecalho += item + '|'
        auxiliar = open('banco_auxiliar1.txt', 'w')
        banco = open(self.nome_banco)
        linha = banco.readline()
        while linha != '':
            auxiliar.write(linha)
            linha = banco.readline()
        auxiliar.close()
        banco.close()
        banco = open(self.nome_banco, 'w')
        auxiliar = open('banco_auxiliar1.txt')
        linha = auxiliar.readline().split('|')
        while linha != ['']:
            linha.insert(posicao, valor_incial)
            banco.write(self.faz_linha(linha))
            linha = auxiliar.readline().split('|')
        auxiliar.close()
        banco.close()

    def deleta_coluna(self, posicao):
        self.regua.pop(posicao)
        self.filtros.pop(posicao)
        novo_cabecalho = self.cabecalho[1:-1].split('|')
        novo_cabecalho.pop(posicao)
        self.cabecalho = '|'
        for item in novo_cabecalho:
            self.cabecalho += item + '|'
        auxiliar = open('banco_auxiliar1.txt', 'w')
        banco = open(self.nome_banco)
        linha = banco.readline()
        while linha != '':
            auxiliar.write(linha)
            linha = banco.readline()
        auxiliar.close()
        banco.close()
        banco = open(self.nome_banco, 'w')
        auxiliar = open('banco_auxiliar1.txt')
        linha = auxiliar.readline().split('|')
        while linha != ['']:
            linha.pop(posicao)
            banco.write(self.faz_linha(linha))
            linha = auxiliar.readline().split('|')
        auxiliar.close()
        banco.close()

    def edita_cabecalho(self, posicao, mudanca=None, nome=None):
        novo_cabecalho = self.cabecalho[1:-1].split('|')
        espacos = novo_cabecalho[posicao].count(' ')
        novo_cabecalho[posicao] = novo_cabecalho[posicao].strip()
        if mudanca is None:
            mudanca = 0
        if nome is not None:
            novo_cabecalho[posicao] = nome
        espacos += mudanca
        self.cabecalho = '|'
        if espacos > 0:
            novo_cabecalho[posicao] = ' ' * (espacos // 2 + espacos % 2) + novo_cabecalho[posicao] + ' ' * (espacos // 2)
        for titulo in novo_cabecalho:
            self.cabecalho += titulo + '|'

    def pega_titulos(self):
        nomes = self.cabecalho[1:-1].split('|')
        return list(nome.strip().capitalize() for nome in nomes)

    def insere_dados(self, dados):
        banco = open(self.nome_banco)
        linha = banco.readline()
        indice = 1
        while linha != '':
            indice = linha.split('|')[0]
            linha = banco.readline()
        banco.close()
        banco = open(self.nome_banco, 'a')
        linha = self.faz_linha([int(indice)+1]+dados)
        banco.write(linha)
        banco.close()

    def deleta_dados(self, indice):
        auxiliar = open('banco_auxiliar1.txt', 'w')
        banco = open(self.nome_banco)
        linha = banco.readline()
        while linha != '':
            auxiliar.write(linha)
            linha = banco.readline()
        auxiliar.close()
        banco.close()
        banco = open(self.nome_banco, 'w')
        auxiliar = open('banco_auxiliar1.txt')
        linha = auxiliar.readline().split('|')
        contador = 0
        while linha != ['']:
            if int(linha[0]) != indice:
                linha[0] = contador
                banco.write(self.faz_linha(linha))
                contador += 1
            linha = auxiliar.readline().split('|')
        auxiliar.close()
        banco.close()

    def edita_dados(self, indice, dados):
        auxiliar = open('banco_auxiliar1.txt', 'w')
        banco = open(self.nome_banco)
        linha = banco.readline()
        while linha != '':
            auxiliar.write(linha)
            linha = banco.readline()
        auxiliar.close()
        banco.close()
        banco = open(self.nome_banco, 'w')
        auxiliar = open('banco_auxiliar1.txt')
        linha = auxiliar.readline().split('|')
        while linha != ['']:
            if int(linha[0]) != indice:
                banco.write(self.faz_linha(linha))
            else:
                banco.write(self.faz_linha([int(indice)]+dados))
            linha = auxiliar.readline().split('|')
        auxiliar.close()
        banco.close()

    def pesquisa_dados(self, indice):
        banco = open(self.nome_banco)
        linha = banco.readline().split('|')
        while linha != ['']:
            if int(linha[0]) == indice:
                banco.close()
                return linha
            linha = banco.readline().split('|')
        banco.close()
        return None

    def organiza_dados(self, criterio):
        if self.regua[criterio] in ['valor', 'indice', 'quantidade', 'numero', 'data']:
            banco = open(self.nome_banco)
            auxiliar1 = open('banco_auxiliar1.txt', 'w')
            linha = banco.readline()
            while linha != '':
                auxiliar1.write(linha)
                linha = banco.readline()
            banco.close()
            auxiliar1.close()
            auxiliares = ['banco_auxiliar1.txt', 'banco_auxiliar2.txt']
            intacto = False
            while not intacto:
                intacto = True
                auxiliares[0], auxiliares[1] = auxiliares[1], auxiliares[0]
                auxiliar1 = open(auxiliares[0], 'w')
                auxiliar2 = open(auxiliares[1])
                linha1 = auxiliar2.readline().split('|')
                while True:
                    linha2 = auxiliar2.readline().split('|')
                    if linha2 == ['']:
                        auxiliar1.write(self.faz_linha(linha1))
                        break
                    if self.regua[criterio] in ['indice', 'numero', 'quantidade', 'valor']:
                        if float(linha1[criterio]) > float(linha2[criterio]):
                            intacto = False
                            auxiliar1.write(self.faz_linha(linha2))
                            linha2 = linha1[:]
                        else:
                            auxiliar1.write(self.faz_linha(linha1))
                    if self.regua[criterio] == 'data':
                        data1 = self.faz_data(linha1[criterio][0:10])
                        data2 = self.faz_data(linha2[criterio][0:10])
                        if int((data1 - data2).days) > 0:
                            intacto = False
                            auxiliar1.write(self.faz_linha(linha2))
                            linha2 = linha1[:]
                        else:
                            auxiliar1.write(self.faz_linha(linha1))
                    linha1 = linha2[:]
                auxiliar1.close()
                auxiliar2.close()
            auxiliar1 = open(auxiliares[0])
            banco = open(self.nome_banco, 'w')
            linha = auxiliar1.readline().split('|')
            contador = 1
            while linha != ['']:
                linha[0] = contador
                banco.write(self.faz_linha(linha))
                linha = auxiliar1.readline().split('|')
                contador += 1
            banco.close()
            auxiliar1.close()

    def mostra_dados(self):
        banco = open(self.nome_banco)
        tamanhos = []
        for coluna in self.cabecalho[1:-1].split('|'):
            tamanhos.append(len(coluna))
        linha = banco.readline()
        print(self.cabecalho)
        while linha != '':
            linha = linha[:-1].split('|')
            linha_formatada = '|'
            if self.aplica_filtros(linha):
                for indice in range(len(linha)):
                    if self.regua[indice] in ['indice', 'quantidade']:
                        linha_formatada += ' ' * (tamanhos[indice] - len(linha[indice])) + linha[indice]
                    if self.regua[indice] == 'valor':
                        linha_formatada += 'R$ ' + ' ' * (tamanhos[indice] - len(f'{float(linha[indice]):.2f}') - 3) + \
                                           f'{float(linha[indice]):.2f}'
                    if self.regua[indice] in ['texto', 'tags']:
                        if tamanhos[indice] - len(linha[indice]) < 0:
                            linha_formatada += linha[indice][:tamanhos[indice]-3] + '...'
                        else:
                            linha_formatada += linha[indice] + ' ' * (tamanhos[indice] - len(linha[indice]))
                    if self.regua[indice] == 'data':
                        linha_formatada += linha[indice][0:tamanhos[indice]]
                    linha_formatada += '|'
                print(linha_formatada)
            linha = banco.readline()

    def pega_indice(self):
        banco = open(self.nome_banco)
        linha = banco.readline()
        indice = 0
        while linha != '':
            indice = linha.split('|')[0]
            linha = banco.readline()
        banco.close()
        return int(indice)

    def faz_linha(self, dados):
        linha = ''
        for dado in dados:
            linha += str(dado) + '|'
        if linha[-2:-1] == '\n':
            return linha[:-1]
        else:
            return linha[:-1] + '\n'

    def faz_data(self, t_data):
        data = t_data.split('/')
        data = date(int(data[2]), int(data[1]), int(data[0]))
        return data

    def aplica_filtros(self, dados):
        for indice in range(len(self.regua)):
            if self.filtros[indice] is None:
                continue
            else:
                if self.regua[indice] == 'texto':
                    if dados[indice] != self.filtros[indice]:
                        return False
                if self.regua[indice] in ['indice', 'numero', 'quantidade', 'valor']:
                    if self.filtros[indice][0] is not None:
                        if float(dados[indice]) < self.filtros[indice][0]:
                            return False
                    if self.filtros[indice][1] is not None:
                        if float(dados[indice]) > self.filtros[indice][1]:
                            return False
                if self.regua[indice] == 'data':
                    data = self.faz_data(dados[indice])
                    if self.filtros[indice][0] is not None:
                        data_inf = self.faz_data(self.filtros[indice][0])
                        if int((data_inf - data).days) > 0:
                            return False
                    if self.filtros[indice][1] is not None:
                        data_sup = self.faz_data(self.filtros[indice][1])
                        if int((data - data_sup).days) > 0:
                            return False
                if self.regua[indice] == 'tags':
                    tags = dados[indice].split(',')
                    for tag in self.filtros[indice]:
                        if tag not in tags:
                            return False
        return True

    def gera_saldos(self, completo=True):
        relevantes = ['corrente itau1',
                      'poupanca itau1',
                      'corrente bb1',
                      'poupanca bb1',
                      'vale alimentacao',
                      'cartao bb2',
                      'bb rf lp high']
        banco = open(self.nome_banco)
        saldos = {}
        linha = banco.readline()[:-1].split('|')
        while linha != ['']:
            faz = False
            if completo:
                faz = True
            else:
                if self.aplica_filtros(linha):
                    faz = True
            if faz:
                if linha[3] not in saldos.keys():
                    saldos[linha[3]] = 0
                if linha[4] not in saldos.keys():
                    saldos[linha[4]] = 0
                saldos[linha[3]] -= float(linha[5])
                saldos[linha[4]] += float(linha[5])
            linha = banco.readline()[:-1].split('|')
        banco.close()
        for conta in list(saldos.keys()):
            if conta in relevantes and saldos[conta] != 0:
                print(f'{conta}: {round(saldos[conta]*100)/100:.2f}')

class FrameDadosVSV(Frame):
    def __init__(self, pai, regua, nomes):
        super().__init__(master=pai)
        self.regua = regua[1:]
        self.nomes = nomes

        self.cont_texto_dados = Frame(self)
        self.cont_texto_dados.grid(row=0, column=0)
        self.cont_campo_dados = Frame(self)
        self.cont_campo_dados.grid(row=0, column=1, pady=2)
        self.labels = []
        self.campos = []

        for linha in range(len(self.regua)):
            self.label_d = 0
            self.campo_d = 0
            if self.regua[linha] == 'data':
                self.label_d = 2
                self.campos.append(DataEntry(self.cont_campo_dados))
                self.campos[linha].grid(row=linha, column=0, pady=self.campo_d)
                self.campos[linha].default()
            else:
                if linha == 0:
                    self.campo_d = 2
                else:
                    self.campo_d = 1
                self.campos.append(Entry(self.cont_campo_dados, width=22))
                self.campos[linha].grid(row=linha, column=0, pady=self.campo_d)
            self.labels.append(Label(self.cont_texto_dados, text=self.nomes[linha]+':'))
            self.labels[linha].grid(row=linha, column=0, pady=self.label_d)

    def pega_dados(self):
        self.dados = []
        for linha in range(len(self.regua)):
            if self.regua[linha] == 'tags':
                self.tags = self.campos[linha].get().split(',')
                self.tags_formatada = self.tags[0]
                for tag in self.tags[1:]:
                    self.tags_formatada += ',' + tag.strip()
                self.dados.append(self.tags_formatada)
            elif self.regua[linha] == 'data':
                self.dados.append(self.campos[linha].pega_data_formatada())
            elif self.regua[linha] == 'valor':
                self.dados.append(f'{float(self.campos[linha].get()):.2f}')
            else:
                self.dados.append(self.campos[linha].get())
        return self.dados

    def insere_dados(self, dados):
        for linha in range(len(self.regua)):
            if self.regua[linha] == 'data':
                self.data = dados[linha].split('/')
                self.data = date(int(self.data[2]), int(self.data[1]), int(self.data[0]))
                self.campos[linha].insere_data(self.data)
            else:
                self.campos[linha].delete(0, END)
                self.campos[linha].insert(0, dados[linha])

class FrameFiltrosVSV(Frame):
    def __init__(self, pai, regua, nomes):
        super().__init__(master=pai)
        self.regua = regua
        self.nomes = nomes

        self.cont_texto_filtros = Frame(self)
        self.cont_texto_filtros.grid(row=0, column=0)
        self.cont_campo_filtros = Frame(self)
        self.cont_campo_filtros.grid(row=0, column=1, pady=2)
        self.labels = []
        self.campos = []
        self.cont = []
        self.linha_extra = 0
        self.campo_extra = 0

        for linha in range(len(self.regua)):
            self.label_d = 0
            self.campo_d = 0
            if self.regua[linha] == 'data':
                self.label_d = 2
                self.campos.append(DataEntry(self.cont_campo_filtros))
                self.campos[linha + self.linha_extra + self.campo_extra].grid(row=linha + self.linha_extra, column=0, pady=self.campo_d)
                self.campos[linha + self.linha_extra + self.campo_extra].insere_data(date(2022, 4, 11))
                self.labels.append(Label(self.cont_texto_filtros, text=self.nomes[linha] + ' ini:'))
                self.labels[linha + self.linha_extra].grid(row=linha + self.linha_extra, column=0, pady=self.label_d)
                self.linha_extra += 1
                self.campos.append(DataEntry(self.cont_campo_filtros))
                self.campos[linha + self.linha_extra + self.campo_extra].grid(row=linha + self.linha_extra, column=0, pady=self.campo_d)
                self.campos[linha + self.linha_extra + self.campo_extra].default()
            else:
                if linha == 0:
                    self.campo_d = 2
                else:
                    self.campo_d = 1
                if self.regua[linha] in ['valor', 'numero', 'quantidade', 'indice']:
                    self.cont.append(Frame(self.cont_campo_filtros))
                    self.cont[-1].grid(row=linha + self.linha_extra, column=0, pady=self.campo_d)
                    self.campos.append(Entry(self.cont[-1], width=10))
                    self.campos[linha + self.linha_extra + self.campo_extra].grid(row=0, column=0)
                    self.campo_extra += 1
                    self.campos.append(Entry(self.cont[-1], width=11))
                    self.campos[linha + self.linha_extra + self.campo_extra].grid(row=0, column=1)
                else:
                    self.campos.append(Entry(self.cont_campo_filtros, width=22))
                    self.campos[linha + self.linha_extra + self.campo_extra].grid(row=linha + self.linha_extra, column=0, pady=self.campo_d)
            if self.regua[linha] != 'data':
                self.labels.append(Label(self.cont_texto_filtros, text=self.nomes[linha] + ':'))
            else:
                self.labels.append(Label(self.cont_texto_filtros, text=self.nomes[linha] + ' fim:'))
            self.labels[linha + self.linha_extra].grid(row=linha + self.linha_extra, column=0, pady=self.label_d)

    def pega_filtros(self):
        filtros = []
        campo = 0
        for tipo in self.regua:
            if tipo in ['quantidade', 'valor', 'numero', 'indice']:
                filtros.append([])
                filtro = self.campos[campo].get()
                if filtro != '':
                    if tipo in ['quantidade', 'indice']:
                        filtros[-1].append(int(filtro))
                    else:
                        filtros[-1].append(float(filtro))
                else:
                    filtros[-1].append(None)
                campo += 1
                filtro = self.campos[campo].get()
                if filtro != '':
                    if tipo in ['quantidade', 'indice']:
                        filtros[-1].append(int(filtro))
                    else:
                        filtros[-1].append(float(filtro))
                else:
                    filtros[-1].append(None)
            elif tipo == 'data':
                filtros.append([])
                datai = self.campos[campo].pega_data_formatada()
                filtros[-1].append(datai)
                campo += 1
                dataf = self.campos[campo].pega_data_formatada()
                filtros[-1].append(dataf)
            elif tipo == 'tags':
                tag = self.campos[campo].get()
                if tag != '':
                    tags = tag.split(',')
                    lista_tags = []
                    for tag in tags:
                        lista_tags.append(tag.strip())
                    filtros.append(lista_tags)
                else:
                    filtros.append(None)
            else:
                filtro = self.campos[campo].get()
                if filtro != '':
                    filtros.append(filtro)
                else:
                    filtros.append(None)
            campo += 1
        return filtros
