## Teachers Models
from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	profile = models.TextField(blank=True)
	photo = models.ImageField(upload_to='teachers', blank=True)

	## Print name on Admin
	def __str__(self):
		return self.first_name