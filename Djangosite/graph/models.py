from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Mittausdata(models.Model):
	id = models.AutoField(primary_key=True)
	aika = models.DateTimeField(auto_now_add=True)
	kosteus = models.DecimalField(max_digits=5, decimal_places=2)
	latitude = models.DecimalField(max_digits=10, decimal_places=5)
	longitude = models.DecimalField(max_digits=10, decimal_places=5)
	def __str__(self):
		return self.aika
	