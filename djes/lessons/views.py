from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Lesson

def lesson_view(request, title):
	lesson = get_object_or_404(Lesson, title=title)

	return HttpResponse('Ok...')

