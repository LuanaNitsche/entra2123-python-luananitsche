from django.shortcuts import render
from .forms import PessoaForm

# Create your views here.
def view_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = PessoaForm()
    
    return render(request, 'teste/viewPessoa.html', {'form': form})