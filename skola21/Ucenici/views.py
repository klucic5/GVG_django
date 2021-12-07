from django.shortcuts import render
from .models import *

def popis_ucenika(request):
    svi_ucenici = Ucenik.dohvati_sve()
    return render(request, 'ucenici_popis.html', {'ucenici':svi_ucenici})


def index(request):
    return render(request, 'index.html')