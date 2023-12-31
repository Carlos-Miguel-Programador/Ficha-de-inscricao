from ttkbootstrap import *
from tkinter import messagebox
from datetime import datetime
from ttkbootstrap import Style
import sqlite3

try:
    banco = sqlite3.connect('componentes/Banco de dados.db')

    cursor = banco.cursor()

    cursor.execute("CREATE TABLE CLASSE_PRE(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_1(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_2(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_3(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_4(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_5(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_6(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_7(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_8(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")
    cursor.execute("CREATE TABLE CLASSE_9(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME VARCHAR(255) NOT NULL, IDADE INT NOT NULL, DATA_DE_NASCIMENTO DATE, GENERO VARCHAR(20) NOT NULL, ENCARREGADO VARCHAR(255) NOT NULL, TELEFONE VARCHAR(30) NOT NULL, MORADA VARCHAR(100) NOT NULL, TIPO_PAGAMENTO VARCHAR(45) NOT NULL, MENSALIDADE DECIMAL(10, 2) NOT NULL, VALOR_INSCRICAO DECIMAL(10, 2) NOT NULL, DATA_INSCRICAO DATETIME NOT NULL)")

    banco.commit()
except:
    pass


def reiniciar(entry1, entry2, entry3, entry4, entry5, entry6, entry7, combo1, combo2, check_a, check_b, mensalidade):
    entry1.set('')
    # entry1.insert('D')
    entry2.set('')
    # entry2.insert('M')
    entry3.set('')
    # entry3.insert('A')
    entry4.set('')
    entry5.set('')
    entry6.set('')
    entry7.set('')
    combo1.current(0)
    combo2.current(0)
    check_a.set(0)
    check_b.set(0)
    mensalidade.set('0.00')


def calc_idade(dt_nascimento):
    idade = int(datetime.now().year) - int(dt_nascimento)
    return idade
def pegando_genero(gen):
    if gen == 'Masculino':
        return 'Masculino'
    elif gen == 'Feminino':
        return 'Feminino'
    else:
        return 'Masculino'
def valor_mensal(classe, val):
    if classe == '1ª classe':
        val.set('1500.00')
        return '1500.00'
    elif classe == '2ª classe':
        val.set('2000.00')
        return '2000.00'
    elif classe == '3ª classe':
        val.set('2000.00')
        return '2000.00'
    elif classe == '4ª classe':
        val.set('2300.00')
        return '2300.00'
    elif classe == '5ª classe':
        val.set('2300.00')
        return '2300.00'
    elif classe == '6ª classe':
        val.set('2500.00')
        return '2500.00'
    elif classe == '7ª classe':
        val.set('2500.00')
        return '2500.00'
    elif classe == '8ª classe':
        val.set('3000.00')
        return '3000.00'
    elif classe == '9ª classe':
        val.set('3500.00')
        return '3500.00'
    elif classe == 'Pré-iniciação':
        val.set('1500.00')
        return '1500.00'
    else:
        val.set('0.00')
        return '0.00'

def valor_mensal1(classe):
    if classe == '1ª classe':
        return '1500.00'
    elif classe == '2ª classe':
        return '2000.00'
    elif classe == '3ª classe':
        return '2000.00'
    elif classe == '4ª classe':
        return '2300.00'
    elif classe == '5ª classe':
        return '2300.00'
    elif classe == '6ª classe':
        return '2500.00'
    elif classe == '7ª classe':
        return '2500.00'
    elif classe == '8ª classe':
        return '3000.00'
    elif classe == '9ª classe':
        return '3500.00'
    elif classe == 'Pré-iniciação':
        return '1500.00'

def tipo_pagamento(t1, t2):
    if t1 == 1:
        return 'Multicaixa'
    else:
        return 'A mão'


def conexao_banco_de_dados(aluno, genero, data, encarregado, morada, telefone, classe, t_pagamento, mensalidade, idade):
    banco = sqlite3.connect('componentes/Banco de dados.db')


    cursor = banco.cursor()

    if classe == 'Classe':
        messagebox.showinfo('Aviso', 'Escolha a classe.')
        return 3
    elif classe == 'Pré-iniciação':
        cursor.execute(f"INSERT INTO CLASSE_PRE(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '2ª classe':
        cursor.execute(f"INSERT INTO CLASSE_2(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '3ª classe':
        cursor.execute(f"INSERT INTO CLASSE_3(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '4ª classe':
        cursor.execute(f"INSERT INTO CLASSE_4(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '5ª classe':
        cursor.execute(f"INSERT INTO CLASSE_5(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '6ª classe':
        cursor.execute(f"INSERT INTO CLASSE_6(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '7ª classe':
        cursor.execute(f"INSERT INTO CLASSE_7(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '8ª classe':
        cursor.execute(f"INSERT INTO CLASSE_8(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '9ª classe':
        cursor.execute(f"INSERT INTO CLASSE_9(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")
    elif classe == '1ª classe':
        cursor.execute(f"INSERT INTO CLASSE_1(NOME, DATA_DE_NASCIMENTO, GENERO, ENCARREGADO, TELEFONE, MORADA, TIPO_PAGAMENTO, MENSALIDADE, VALOR_INSCRICAO, DATA_INSCRICAO, IDADE) VALUES('{aluno}', '{data}', '{genero}', '{encarregado}', '{telefone}', '{morada}', '{t_pagamento}', {mensalidade}, {750.00}, '{datetime.now()}', {idade})")

    banco.commit()


def fazer_inscricao(aluno, genero, dia, mes, ano, encarregado, morada, telefone, classe, t_pagamento1, t_pagamento2, mensalidade):
    if (aluno, genero, dia, mes, ano, encarregado, morada, telefone, classe, mensalidade) != '' and t_pagamento2 != 0 or t_pagamento1 != 0:
        # TRABALHANDO COM A DATA DE NASCIMENTO
        data_nascimento = ano + '-' + mes + '-' + dia

        # TRABALHANDO COM O VALOR MENSAL
        vl = valor_mensal1(classe)

        # TRABALHANDO COM TIPO DE PAGAMENTO
        t_pag = tipo_pagamento(t_pagamento1, t_pagamento1)

        # TRABALHANDO COM A IDADE
        idade = calc_idade(ano)

        # TRABALHANDO COM GENERO
        gn = pegando_genero(genero)

        conexao_banco_de_dados(aluno.strip().title(),
                               gn,
                               data_nascimento,
                               encarregado.strip().title(),
                               morada.strip().title(),
                               '(+244)' + telefone.strip(),
                               classe,
                               t_pag,
                               vl,
                               idade
                               )
        if classe != 'Classe':
            messagebox.showinfo('Aviso', aluno.strip().title() + ' foi inscrito(a) com sucesso!')
            reiniciar(e_d, e_ms, e_an, e_m, e_f, e_acg, e_mr, combo_c, combo_g, valor_check1, valor_check2, valor)

    else:
        messagebox.showinfo('Aviso', 'Ocorreu, é necessário que todos os campos estejam preenchidos!')

def cancelar(window):
    window.destroy()

# CONFIGURAÇÃO DA JANELA
janela = Window()
Style('cyborg')
janela.geometry('500x500+400+100')
janela.resizable(0, 0)
janela.iconbitmap('componentes/icon.ico')
janela.title('Ficha de inscrição')

# PRIMEIRO ELEMENTO DA MINHA JANELA

# CONFIGURAÇÃO DA LABEL FRAME
label_frame = LabelFrame(janela, text='Obtendo dados')
label_frame.place(x=20, y=30, height=220, width=460)

# CONFIGURAÇÃO DA ENTRADA DO NOME
label = Label(label_frame, text='Nome:', font=('Times new Roman', 15))
label.place(x=5, y=10)

e_m = StringVar()
entry_nome = Entry(label_frame, textvariable=e_m, font=('Times new Roman', 12), width=25)
entry_nome.place(x=5, y=40)

# CONFIGURAÇÃO DO GENERO
combo_g = Combobox(label_frame)
combo_g['values'] = ['Gênero', 'Masculino', 'Feminino']
combo_g.current(0)
combo_g.place(x=5, y=80)

# CONFIGURAÇÃO DA DATA DE NASCIMENTO
label = Label(label_frame, text='Data de nascimento:', font=('Times new Roman', 15))
label.place(x=5, y=120)

e_d = StringVar()
entry_dia = Entry(label_frame, textvariable=e_d, font=('Times new Roman', 12), width=2)
entry_dia.place(x=5, y=159)
entry_dia.insert(0, 'D')

e_ms = StringVar()
entry_mes = Entry(label_frame, textvariable=e_ms, font=('Times new Roman', 12), width=2)
entry_mes.place(x=45, y=159)
entry_mes.insert(0, 'M')

e_an = StringVar()
entry_ano = Entry(label_frame, textvariable=e_an, font=('Times new Roman', 12), width=5)
entry_ano.place(x=85, y=159)
entry_ano.insert(0, 'A')

# CONFIGURAÇÃO DA MORADA
label_morada = Label(label_frame, text='Morada:', font=('Times new Roman', 15))
label_morada.place(x=240, y=10)

e_mr = StringVar()
entry_morada = Entry(label_frame, textvariable=e_mr, font=('Times new Roman', 12), width=25)
entry_morada.place(x=240, y=40)

# CONFIGURAÇÃO NOME DO ENCARREGADO
label_encarregado = Label(label_frame, text='Encarregado(a):', font=('Times new Roman', 15))
label_encarregado.place(x=240, y=80)

e_acg = StringVar()
entry_encarregado = Entry(label_frame, textvariable=e_acg, font=('Times new Roman', 12), width=25)
entry_encarregado.place(x=240, y=115)

# CONFIGURAÇÃO DO TELEFONE DO ENCARREGADO
label_fone = Label(label_frame, text='fone:', font=('Times new Roman', 15))
label_fone.place(x=240, y=165)

e_f = StringVar()
entry_fone = Entry(label_frame, textvariable=e_f, font=('Times new Roman', 12), width=int(18.5+0.3))
entry_fone.place(x=296, y=160)

# PRIMEIRO ELEMENTO DA MINHA JANELA

# SEGUNDO ELEMENTO DA MINHA JANELA

# LABEL FRAME 2
label_frame1 = LabelFrame(janela, text='Fazendo a inscrição')
label_frame1.place(x=20, y=270, height=180, width=460)

# CONFIGURANDO A CLASSE

combo_c = Combobox(label_frame1)
combo_c['values'] = ('Classe',
                   'Pré-iniciação',
                   '1ª classe',
                   '2ª classe',
                   '3ª classe',
                   '4ª classe',
                   '5ª classe',
                   '6ª classe',
                   '7ª classe',
                   '8ª classe',
                   '9ª classe')
combo_c.current(0)
combo_c.place(x=5, y=10)

# CONFIGURANDO O TEXTO DA MENSALIDADE

label_mensalidade = Label(label_frame1, text='Mensalidade:', font=('Times new Roman', 15))
label_mensalidade.place(x=240, y=14)

valor = StringVar()
valor.set('0.00')
label_valor = Label(label_frame1, textvariable=valor, font=('Times new Roman', 17))
label_valor.place(x=240, y=40)

# CONFIGURANDO TIPO DE PAGAMENTO

label_tipo_pagamento = Label(label_frame1, text='Tipo de pagamento', font=('Times new Roman', 15))
label_tipo_pagamento.place(x=5, y=45)

valor_check1 = IntVar()
check1 = Checkbutton(label_frame1, variable=valor_check1, text='Multicaixa', bootstyle='')
check1.place(x=5, y=85)

valor_check2 = IntVar()
check2 = Checkbutton(label_frame1, text='A mão', variable=valor_check2)
check2.place(x=5, y=115)

# CONFIGURANDO O BOTÃO FAZER INSCRIÇÃO

botao_inscricao = Button(janela, text='Fazer inscrição', style=PRIMARY, width=17, command=lambda: fazer_inscricao(entry_nome.get(),
                                                                                                                  combo_g.get(),
                                                                                                                  entry_dia.get(),
                                                                                                                  entry_mes.get(),
                                                                                                                  entry_ano.get(),
                                                                                                                  entry_encarregado.get(),
                                                                                                                  entry_morada.get(),
                                                                                                                  entry_fone.get(),
                                                                                                                  combo_c.get(),
                                                                                                                  valor_check1.get(),
                                                                                                                  valor_check2.get(),
                                                                                                                  valor.get()
                                                                                                                  ))
botao_inscricao.place(x=120, y=450)

botao_cancelar = Button(janela, text='Cancelar inscrição', style=DANGER, width=17, command=lambda: cancelar(janela))
botao_cancelar.place(x=250, y=450)

botao_ver_mensalidade = Button(janela, text='ver mensalidade', style=SECONDARY, command=lambda: valor_mensal(combo_c.get(), valor))
botao_ver_mensalidade.place(x=260, y=390)


janela.mainloop()