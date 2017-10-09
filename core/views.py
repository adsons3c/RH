from django.shortcuts import render, redirect, get_object_or_404
from core.forms import PerfilForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from core.models import Perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#@login_required
def cadastro(request):
	if request.method == 'POST':
		form = PerfilForm(request.POST)
		if form.is_valid():
			user = form.save()
			perfil = Perfil()
			perfil.data_nascimento = form.cleaned_data.get('data_nascimento')
			perfil.cpf = form.cleaned_data.get('cpf')
			perfil.filial = form.cleaned_data.get('filial')
			perfil.setor = form.cleaned_data.get('setor')
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

def home(request):
	return render(request, 'home.html')

def listar(request):
	users = User.objects.all()
	return render(request, 'listar_users.html', {'users':users})

def delete(request,pk, template_name='confirm_delete.html'):
	user = get_object_or_404(User, pk=pk)
	if request.mothod == "POST":
		user.delete()
		user.perfil.delete()
		return redirect('listar')
	return render(request, template_name, {'object':user})

def atualizar(request, pk, template_name='atuallizar.html'):
	user = 	get_object_or_404(Perfil, pk=pk)
	form = PerfilForm(request.POST or None, instance=user)
	if form.is_valid:
		form.save()
		return redirect('listar')
	return render(request,template_name,{'form':form, 'user':user})
