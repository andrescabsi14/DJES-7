## Lessons Models
from django.db import models


class Lesson(models.Model):
	order = models.PositiveIntegerField()
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='lessons', blank=True)
	lesson_file = models.FileField(upload_to='lessons')
