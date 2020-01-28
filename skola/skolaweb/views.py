from django.shortcuts import render
from django.http import *
from skolaweb.models import *
from skolaweb.forms import *

# Create your views here.
def ucenici_add(request):
	if request.method=='POST':
		data=UcenikForm(request.POST)
		if (data.is_valid()):
			data.save()
			return HttpResponseRedirect('/skolaweb/ucenici')
		else:
			return render(request,'ucenici_form.html',{'form':data})
	else:
		form=UcenikForm()
		return render(request,'ucenici_form.html',{'form':form})
	
def ucenici_index(request):
	data=Ucenik.objects.all().order_by('Prezime')
	podatci={'data':data}
	return render(request,'ucenici_index.html',podatci)
	
def index(request):
	return render(request,'index.html')

	
