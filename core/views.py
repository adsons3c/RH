from django.shortcuts import render, redirect
from core.forms import PerfilForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from core.models import Perfil
from django.contrib.auth.decorators import login_required

@login_required
def cadastro(request):
	if request.method == 'POST':
		form = PerfilForm(request.POST)
		if form.is_valid():
			user = form.save()
			perfil = Perfil()
			perfil.data_nascimento = form.cleaned_data.get('data_nascimento')
			perfil.cpf = form.cleaned_data.get('cpf')
			perfil.filial = form.cleaned_data.get('filial')
			perfil.vinculo = form.cleaned_data.get('vinculo')
			perfil.cargo = form.cleaned_data.get('cargo')
			perfil.mae = form.cleaned_data.get('mae')
			perfil.pai = form.cleaned_data.get('pai')
			perfil.estado_civil = form.cleaned_data.get('estado_civil')
			perfil.laudo = form.cleaned_data.get('laudo')
			perfil.rua = form.cleaned_data.get('rua')
			perfil.numero = form.cleaned_data.get('numero')
			perfil.bairro = form.cleaned_data.get('bairro')
			perfil.cep = form.cleaned_data.get('cep')
			perfil.cidade = form.cleaned_data.get('cidade')
			perfil.estado = form.cleaned_data.get('estado')			
			perfil.user = user
			perfil.save()
			messages.success(request, ('User created successfull'))
			return redirect('/cadastro')
		
		else:
			messages.error(request, ('Please correct the error below.'))

	else:
		form = PerfilForm()

	return render(request, 'cadastro.html', {'form': form})


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], 
							password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/cadastro')
	return render(request, 'login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')