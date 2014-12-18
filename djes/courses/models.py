## Courses Models
from django.db import models

from teachers.models import Teacher 

class Course(models.Model):
	title = models.CharField(max_length=255)
	cover = models.ImageField(upload_to='courses', blank=True)
	teacher = models.ForeignKey(Teacher)