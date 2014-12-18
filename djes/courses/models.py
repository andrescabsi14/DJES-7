## Courses Models
from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='courses')
	teacher = 