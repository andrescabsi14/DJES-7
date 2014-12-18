## Lessons Models
from django.db import models

from courses.models import Course
from teachers.models import Teacher

class Lesson(models.Model):
	order = models.PositiveIntegerField()
	title = models.CharField(max_length=255)
	image = models.ImageField(upload_to='lessons', blank=True)
	lesson_file = models.FileField(upload_to='lessons')
	course = models.ForeignKey(Course, blank=True)
	teacher = models.ForeignKey(Teacher, blank=True)

	## Print name on Admin
	def __str__(self):
		return self.title