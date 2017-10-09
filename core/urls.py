from django.conf.urls import url
from core import views 

urlpatterns = [
	url(r'^cadastro/$', views.cadastro, name='cadastro'),
	url(r'^login/$', views.do_login, name='login'),
	url(r'^logout/$', views.do_logout, name='logout'),
	url(r'^home/$', views.home, name='home'),
	url(r'^listar/$', views.listar, name='listar'),
	url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
	url(r'^atualizar/(?P<pk>\d+)$', views.atualizar, name='atualizar'),
]