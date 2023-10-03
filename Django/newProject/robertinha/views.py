from django.shortcuts import render, HttpResponse, redirect
from .forms import ContatoForm, Ex003Form, QuestionForm, Ex007Form
from datetime import datetime
from .compras import compras

def ex002(request):
    context = {
        'minha_string' : 'Olá mundo',
        'meu_inteiro' : 123,
        'meu_booleano' : True,
        'meu_lista' : [1,2,3,4,5],
        'meu_dicionario' : {'a':1, 'b':2, 'c':3},
        'meu_objeto' : {'nome': 'Angelica', 'idade': 23},
        'meu_arquivo' : 'angelica/ex002.html',
        'meu_arquivo_html' : 'angelica/ex002.html',
        'meu_arquivo_css' : 'angelica/ex002.css',
    }
    return render(request, 'robertinha/ex002.html', context)


def qualquer(valor):
    return valor.upper()


def index(request):
    #return HttpResponse("hello world")
    return render(request, 'robertinha/index.html')

def ex002(request):
    context = {
        'minha_string': 'Olá, Mundo!',
        'meu_inteiro': 123,
        'meu_booleano': True
    }
    return render(request, 'robertinha/ex002.html', context)

def contato(request):  
    # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')
    assunto = ""

    if request.method == 'POST':
        metodo = "*POST*"
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            assunto = qualquer(assunto) #add 
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email, idade) #retiramos qualquer(idade)
        

    else:
        metodo = "*GET*"
        initial_data = {                    #Lista que define e coloca dentro das caixas de texto,  
            'assunto': 'Tópico Padrão',         #uma mensagem inicial
            'texto': 'Texto Padrão',
            'email': 'email@exemplo.com',
            'idade': 30,
            
        }
        form = ContatoForm(initial=initial_data) 

    context = { 
        'titulo' : 'História do passos',
        'passo' : 'Passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
        'resposta' : assunto
    }
    
    return render(request, 'robertinha/contato.html', context)


def index(request):    
    return render(request, 'robertinha/index.html')


def ex003(request):
    ip_adress = request.META.get('REMOTE_ADDR')
    msg = ""

    if request.method == 'POST':
        form = Ex003Form(request.POST, initial={'pergunta': 'Qual é a capital da França?'}) #para não sumir a pergunta durante o post
        if form.is_valid():
            resposta = form.cleaned_data['resposta']
            if resposta == 'A': 
                msg = "Parabéns, você acertou!"
            else:
                msg = "Ops, tente novamente."
    else:
        form = Ex003Form(initial={'pergunta': 'Qual é a capital da França?'})
        msg = ""

    context = { 
        'form' : form,
        'msg' : msg,
        
    }


    return render(request, 'robertinha/ex003.html', context)

def ex004(request):
    dicionario = {
		    '1': {
		        'Q': 'Qual é a linguagem de programação criada por Guido van Rossum?',
		        'A': 'Java',
		        'B': 'Python',
		        'C': 'C++',
		        'D': 'Ruby',
		        'R': 'B'
		    },
		    '2': {
		        'Q': 'Em que ano foi lançado o primeiro iPhone?',
		        'A': '2004',
		        'B': '2007',
		        'C': '2010',
		        'D': '2001',
		        'R': 'B'
		    },
		    '3': {
		        'Q': 'Quem escreveu "Dom Quixote"?',
		        'A': 'William Shakespeare',
		        'B': 'Miguel de Cervantes',
		        'C': 'Fyodor Dostoevsky',
		        'D': 'Charles Dickens',
		        'R': 'B'
		    },
		    '4': {
		        'Q': 'Qual é a capital do Brasil?',
		        'A': 'Rio de Janeiro',
		        'B': 'São Paulo',
		        'C': 'Brasília',
		        'D': 'Salvador',
		        'R': 'C'
		    },
		    '5': {
		        'Q': 'O que o GIT faz?',
		        'A': 'Editor de Texto',
		        'B': 'Sistema de Versionamento',
		        'C': 'Navegador Web',
		        'D': 'Sistema Operacional',
		        'R': 'B'
		    },
		    '6': {
		        'Q': 'Qual é a fórmula da água?',
		        'A': 'CO2',
		        'B': 'O2',
		        'C': 'H2O',
		        'D': 'CH4',
		        'R': 'C'
		    },
		    '7': {
		        'Q': 'Quem pintou a Mona Lisa?',
		        'A': 'Vincent van Gogh',
		        'B': 'Pablo Picasso',
		        'C': 'Michelangelo',
		        'D': 'Leonardo da Vinci',
		        'R': 'D'
		    },
		    '8': {
		        'Q': 'Qual é o maior planeta do sistema solar?',
		        'A': 'Vênus',
		        'B': 'Marte',
		        'C': 'Júpiter',
		        'D': 'Saturno',
		        'R': 'C'
		    },
		    '9': {
		        'Q': 'Em que ano terminou a Segunda Guerra Mundial?',
		        'A': '1945',
		        'B': '1950',
		        'C': '1939',
		        'D': '1960',
		        'R': 'A'
		    },
		    '10': {
		        'Q': 'Qual é o nome da famosa série de TV sobre motociclistas fora da lei?',
		        'A': 'Breaking Bad',
		        'B': 'Game of Thrones',
		        'C': 'Sons of Anarchy',
		        'D': 'The Sopranos',
		        'R': 'C'
		    }
		}
    acesso = len(dicionario)

    if request.method == 'POST':
        form = QuestionForm(dicionario, request.POST)
        if form.is_valid():
            respostas = form.cleaned_data
            acertos = {key: value['R'] for key, value in dicionario.items()}
            
            # Calculate the pontuacao
            pontuacao = sum([1 for key, value in respostas.items() if value == acertos[key]])
            
            context = {
                'dic': dicionario,
                'respostas': respostas,
                'acertos': acertos,
                'pontuacao': pontuacao,
                'acesso' : acesso
                
            }

            return render(request, 'robertinha/results.html', context) # quando for requisitado para postar
    else:
        form = QuestionForm(dicionario)

    context = {
        'dic': dicionario,
        'form': form, #arquivo forms.py -> QuestionForm
    }

    return render(request, 'robertinha/ex004.html', context) #quando é requisitado apenas leitura

  
def ex005(request):
    pessoas = {
        1: {'nome': 'Lucas Ferrari', 'cep': '89000'},
        2: {'nome': 'Rafaela Weiss', 'cep': '89010'},
        3: {'nome': 'Ana Rossi', 'cep': '89020'},
        4: {'nome': 'Carlos Müller', 'cep': '89030'},
        5: {'nome': 'Fernanda Schmidt', 'cep': '89040'},
        6: {'nome': 'Gabriela Bianchi', 'cep': '89050'},
        7: {'nome': 'Rodrigo Meier', 'cep': '89060'},
        8: {'nome': 'Isabela Romano', 'cep': '89070'},
        9: {'nome': 'Mateus Klein', 'cep': '89080'},
        10: {'nome': 'Juliana Martini', 'cep': '89090'},
    }

    cidades = {
        '89000': {'nome': 'Gaspar', 'estado': 'SC'},
        '89010': {'nome': 'Ilhota', 'estado': 'SC'},
        '89020': {'nome': 'Rodeio', 'estado': 'SC'},
        '89030': {'nome': 'Ascurra', 'estado': 'SC'},
        '89040': {'nome': 'Blumenau', 'estado': 'SC'},
        '89050': {'nome': 'Indaial', 'estado': 'SC'},
        '89060': {'nome': 'Timbó', 'estado': 'SC'},
        '89070': {'nome': 'Pomerode', 'estado': 'SC'},
        '89080': {'nome': 'Brusque', 'estado': 'SC'},
        '89090': {'nome': 'Guabiruba', 'estado': 'SC'},
    }

    pessoas_com_cidades = {}

    for id_pessoa, info in pessoas.items():
        cep = info['cep']
        cidade_info = cidades.get(cep, "Cidade não encontrada")

        if cidade_info != "Cidade não encontrada":
            pessoas_com_cidades[id_pessoa] = {
                'nome': info['nome'],
                'cidade': cidade_info['nome'],
                'estado': cidade_info['estado']
            }
        else:
            pessoas_com_cidades[id_pessoa] = {
                'nome': info['nome'],
                'cidade': 'Desconhecida',
                'estado': 'Desconhecido'
            }

    return render(request, 'robertinha/ex005.html', {'pessoas_com_cidades': pessoas_com_cidades})

  
  
def mercado(request):
    if request.method == 'POST':
        pass
    else:
        produtos ={
            '1':{'nome':'Arroz',
                 'id_for' : '11',
                 'id_cat' : '202', 
                 'id_estoque' : '02', 
                 'id_vcto' : datetime(2022, 10, 5),                                 #usando a biblioteca datetime para definir uma data de validade
                 'dias_vencidos' : calculo_vencimento(datetime(2022, 10, 5))},      #implementando a funcao de calculo para vencimento

            '2':{'nome':'Papel higiênico',
                 'id_for' : '22',
                 'id_cat' : '404', 
                 'id_estoque' : '01', 
                 'id_vcto' : datetime(2023, 10, 2), 
                 'dias_vencidos' : calculo_vencimento(datetime(2023, 10, 2))},        

            '3':{'nome':'MI9',
                 'id_for' : '33',
                 'id_cat' : '505', 
                 'id_estoque' : '03', 
                 'id_vcto' : '030', 
                 'id_vcto' : datetime(2023, 10, 5),
                 'dias_vencidos' : calculo_vencimento(datetime(2023, 10, 5))}
        }
        
        fornecedores = {
            '11' : {'nome' : 'Alimentos do Sul'},
            '22' : {'nome' : 'Neve'},
            '33' : {'nome' : 'Xiaomi'}
        }
        
        categoria = {
            '202' : {'nome' : 'Alimentos'},
            '404' : {'nome' : 'Produtos de higiene'},
            '505' : {'nome' : 'Eletrônicos'}
        }
        
        estoque = {
            '01' : {'localizacao' : 'Prateleira A1', 'saldo' : '2'},
            '02' : {'localizacao' : 'Prateleira A5', 'saldo' : '0'},
            '03' : {'localizacao' : 'Prateleira D2', 'saldo' : '10'}
        }

        novoDic = {}
        lista_dias_vencidos = []                   #inicia a lista para futuro armazenamento dos dias
        
        for id_produtos, info in produtos.items(): #id_produtos = chave, info = dic de info de produto
            id_for = info['id_for']                #pega id do fornecedor
            id_cat = info['id_cat']                #pega id da categoria
            id_estoque = info ['id_estoque']       #pega id do fornecedor
            id_vcto = info['id_vcto']
        
            
            
            nome_prod = info['nome']
            dias_vencidos = calculo_vencimento(info['id_vcto'])           #pega o nome do produto a partir da info
            
            lista_dias_vencidos.append(dias_vencidos)                     #armazena os dias vencidos de cada produto dentro de uma lista
            
            nome_for = fornecedores.get(id_for, {}).get('nome', 'Desconhecida')     #pega o nome do fornecedor com base na id dele
            nome_cat = categoria.get(id_cat, {}).get('nome', 'Desconhecida')        #pega o nome da categoria com base na id dela
            local = estoque.get(id_estoque, {'localizacao' : 'Desconhecida', 'saldo' : '0'}) #pega a localizacao e o saldo com base no id do estoque
            novoDic[id_produtos] = {               #popula o novo dicionario com as infos que coletamos acima com o .get
                'Produto' : nome_prod,        #associa a chave (nome_produto) ao nome no dicionario (nome_prod)
                'Fornecedor' : nome_for,      #faz o mesmo com fornecedor, categoria, localizacao, saldo, vencimento, media, datavalidade
                'Categoria' : nome_cat,
                'Localização' : local['localizacao'],
                'Saldo' : local['saldo'],
                'DataValidade': formatar_data_brasileira(id_vcto),
                'Vencimento' : dias_vencidos,
                'MediaVencimento' : dias_vencidos
            }
        if lista_dias_vencidos:
            media_dias_vencidos = sum(lista_dias_vencidos) / len(lista_dias_vencidos)       #cria var para armazenar a soma dos dias dividido pela quantidade de dias armazenados na lista
            media_dias_vencidos = round(media_dias_vencidos, 2)                             #formata o número para 2 digitos após a vírgula
            if media_dias_vencidos < 0:                                                     #deixa os dias no formato positivo
                media_dias_vencidos = abs(media_dias_vencidos)
        else:
            media_dias_vencidos = 0                                                         #se a lista estiver vazia, retorna vazio
        
        print(novoDic)   
    
        return render(request, 'robertinha/ex006.html', {'novoDic': novoDic, 'media_dias_vencidos': media_dias_vencidos})  #imprime o novoDicionario e a media de vencimento
  
  
def calculo_vencimento(id_vcto):
    data_vcto = id_vcto                         #recebe a data de validade
    data_hoje = datetime.now()                  #recebe a data de hoje

    if data_vcto <= data_hoje:                  #compara se a data de validade é menor que a data de hoje
        dias_vencidos = (data_vcto - data_hoje).days        #guarda o resultado da subtracao na var dias_vencidos
        dias_vencidos = abs(dias_vencidos)                  #deixa no formato positivo
    else:
        dias_vencidos = 0  # Se a data de validade já passou, definimos dias_vencidos como 0
    return dias_vencidos


def formatar_data_brasileira(data):
    if data is None:                    #se nao tem data, nao formata
        return ""
    return data.strftime("%d/%m/%Y")    #formata no formato d/m/y (brasileiro)




def ex007(request):
    if request.method == 'POST':
        form = Ex007Form(request.POST)

        if form.is_valid():
            id_produto = form.cleaned_data['id_produto']
            nome_produto = form.cleaned_data['nome_produto']
            qnt_produto = form.cleaned_data['qnt_produto']

            compras[id_produto] = {'nome': nome_produto, 'qnt': qnt_produto}

    else:
        form = Ex007Form()
    
    context = {
    'lista_de_compras': compras, 
    'form': form   
    }
    
    return render(request, 'robertinha/ex007.html', context )


def ex007_add(request):
    if request.method == 'POST':
        form = Ex007Form(request.POST)
        if form.is_valid():
            nome_produto = form.cleaned_data['nome_produto']
            qnt_produto = form.cleaned_data['qnt_produto']

            proximo_id = str(len(compras) + 1)

            compras[proximo_id] = {'nome': nome_produto, 'qnt': qnt_produto}

            return redirect('robertinha:ex007')

    else:
        proximo_id = str(len(compras) + 1)
        form = Ex007Form(initial={'id_produto': proximo_id})

    return render(request, 'robertinha/ex007_add.html', {'form': form})



def ex007_remove(request, id_produto):
    if request.method == 'POST':
        if id_produto in compras:
            print (compras[id_produto])
            del compras[id_produto]
    return redirect('robertinha:ex007')