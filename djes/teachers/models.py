## Teachers Models
from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	profile = models.TextField(blank=True)
