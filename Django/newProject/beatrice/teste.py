def contato(request):  
    # coletar o endereco IP do client (pessoa que acessado esta view)
    ip_address = request.META.get('REMOTE_ADDR')
    
    if request.method == 'POST':
        metodo = "*POST*"
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            assunto = qualquer(assunto)  # Aqui estamos chamando a função qualquer
            texto = form.cleaned_data['texto']
            email = form.cleaned_data['email']
            idade = int(form.cleaned_data['idade'])
            print(assunto, texto, email, idade)

    else:
        metodo = "*GET*"
        initial_data = {
            'assunto': 'Tópico Padrão',
            'texto': 'Texto Padrão',
            'email': 'email@exemplo.com',
            'idade': 30,
        }
        form = ContatoForm(initial=initial_data)

    context = { 
        'titulo': 'História dos passos',
        'passo': 'Passo 1',
        'metodo': metodo,
        'ip_address': ip_address,
        'form': form,
    }
    
    return render(request, 'angeline/contato.html', context)

def qualquer(valor):
    return valor.upper()