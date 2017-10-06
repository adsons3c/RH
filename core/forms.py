from django import forms
from core.models import Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class PerfilForm(UserCreationForm):
	data_nascimento = forms.DateField()
	cpf = forms.CharField(max_length=11)
	filial = forms.CharField(max_length=30)
	vinculo = forms.CharField(max_length=20)
	cargo = forms.CharField(max_length=20)
	mae = forms.CharField(max_length=150)
	pai = forms.CharField(max_length=150)
	estado_civil = forms.CharField(max_length=30)
	laudo = forms.CharField(widget=forms.Textarea)
	rua = forms.CharField(max_length=200)
	numero = forms.IntegerField()
	bairro = forms.CharField(max_length=100)
	cep = forms.IntegerField()
	cidade = forms.CharField(max_length=50)
	estado = forms.CharField(max_length=30)

	class Meta:
		model = User
		fields = ('first_name', 'username', 'password1', 'password2')

