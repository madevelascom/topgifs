from django.db import models

class Gif(models.Model):
	id = models.IntegerField(primary_key=True)
	url = models.TextField(null=False, default='#')
	descripcion = models.TextField(default='')
	contador = models.IntegerField(null=False,default='0')

	def __str__(self):  #
		return self.url