from django.db import models

class Ucenik(models.Model):
	Ime=models.CharField(max_length=20)
	Prezime =models.CharField(max_length=20)
	DatumRodenja=models.DateField()
	def __repr__(self):
		return self.Ime+' '+ self.Prezime

