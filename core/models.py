from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



FILIAL = (
	('Acre','Acre'),
	('Alagoas', 'Alagoas'),
	('Amapá', 'Amapá'),
	('Amazonas', 'Amazonas'), 
	('Bahia', 'Bahia'),
	('Paraiba', 'Paraiba'),

)

SETOR = (

	('Informatica', 'Informatica'),
	('Recursos Humanos', 'Recursos Humanos'),
	('Juridico', 'Juridico'),
	('Design', 'Design'),
	('Administrador', 'Administrador'),

)


VINCULO = (

	('Em Serviço', 'Em Serviço'),
	('Dispensado', 'Dispensado'),

	)

CARGO = (

	('Desenvolvedor', 'Desenvolvedor'),
	('DEV', 'DEV'),
	('Advogado', 'Advogado'),
	('Contador', 'Contador')
	
)

CIVIL = (
	('Solteiro', 'Solteiro'),
	('Casado', 'Casado'),
	('Viuvo', 'Viuvo'),	
)


class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	data_nascimento = models.DateField(null=True, blank=True)
	cpf = models.CharField(max_length=11, unique=True)
	filial = models.CharField(max_length=30, choices=FILIAL)
	setor = models.CharField(max_length=40, choices=SETOR)
	vinculo = models.CharField(max_length=20, choices=VINCULO)
	cargo = models.CharField(max_length=20, choices=CARGO)
	mae = models.CharField(max_length=150)
	pai = models.CharField(max_length=150)
	estado_civil = models.CharField(max_length=30, choices=CIVIL)
	laudo = models.TextField()
	rua = models.CharField(max_length=200)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100)
	cep = models.IntegerField()
	cidade = models.CharField(max_length=50)
	estado = models.CharField(max_length=30)
	
	

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Perfil.objects.create(user=instance)
# 		instance.perfil.save()

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.funcionario.save()
