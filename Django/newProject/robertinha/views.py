from django.shortcuts import render, HttpResponse, redirect
from .forms import ContatoForm, Ex003Form, QuestionForm


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
        'titulo' : 'historia do passos',
        'passo' : 'passo 1',
        'metodo' : metodo,
        'ip_address' : ip_address,
        'form' : form,
        #'resposta' : assunto
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

# def contato2(request):  
#     # coletar o endereco IP do client (pessoa que acessado esta view)
#     ip_address = request.META.get('REMOTE_ADDR')

#     if request.method == 'POST':
#         metodo = "*post*"
#     else:
#         metodo = "*get*"
#         initial_data = {                    #Lista que define e coloca dentro das caixas de texto,  
#             'assunto': 'Tópico Padrão',         #uma mensagem inicial
#             'texto': 'Texto Padrão',
#             'email': 'email@exemplo.com',
#             'idade': 30,
#         }
#         form = ContatoForm(initial=initial_data) 

#     context = { 
#         'titulo' : 'historia do passos',
#         'passo' : 'passo 1',
#         'metodo' : metodo,
#         'ip_address' : ip_address
#     }
#     return render(request, 'robertinha/contato2.html', context)

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
#print(dicionario)
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

    # for chave in dicionario.keys():               #percorre apenas as chaves
    #     print(chave)
        
    # for x in dicionario.values():          #percorre apenas os valores
    #     print(x)   
    
    # for x in dicionario.values():      #percorre valores e opcoes de resposta
    #     for y in x.values():
    #         print(y)
    












# question_number = request.GET.get('question_number')
# return render(request, 'robertinha/ex004.html', {'quest': questions, 'question_number': question_number})
  
#   if request.method == 'POST':
#         form = QuestionForm(questions, request.POST)
#         if form.is_valid():
#             pergunta = form.cleaned_data['Q']
#             results = form.cleaned_data  # Get user's answers
#             return render(request, 'robertinha/results.html', {'results': results})
#     else:
#         form = QuestionForm(questions)

#     context = {
#         'form': form,
#         'questions': questions,
#     }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    # if request.method == 'POST':
    #     form = QuestionForm(questions, request.POST)
    #     if form.is_valid():
    #         pergunta = form.cleaned_data['Q']
    #         results = form.cleaned_data  # Get user's answers
    #         return render(request, 'robertinha/results.html', {'results': results})
    # else:
    #     form = QuestionForm(questions)

    # context = {
    #     'form': form,
    #     'questions': questions,
    # }

    # return render(request, 'robertinha/ex004.html', context)
