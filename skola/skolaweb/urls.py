from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^ucenici/add',views.ucenici_add, name='uc_add'),
	url(r'^ucenici/',views.ucenici_index, name='uc_index'),
	url(r'^$',views.index, name='index'),
	]