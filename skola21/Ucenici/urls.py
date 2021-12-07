from django.urls import path 
from . import views

urlpatterns = [ 
    path('ucenici/', views.popis_ucenika, name='popis-ucenika'),
    path('', views.index, name='ucenici-index')
]
