from django.forms import ModelForm
from skolaweb.models import *

class UcenikForm(ModelForm):
	class Meta:
		model=Ucenik
		fields='__all__'
		
#umjesto fields='__all__' mogli smo staviti fields=['Ime','Prezime']

		