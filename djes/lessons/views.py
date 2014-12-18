from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Lesson

def lesson_view(request, title):
	try:
		lesson = Lesson.objects.get(title=title)
	except Lesson.DoesNotExist:
		raise Http404
		
	return HttpResponse('Ok...')

