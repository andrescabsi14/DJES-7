from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Lesson

def lesson_view(request, title):
	##Return 404 if not exist
	lesson = get_object_or_404(Lesson, title=title)
	##Custom Variables for view
	bio = lesson.teacher.profile
	##Return lesson if exist
	return render(request, 'lesson.html', {'lesson': lesson, 'bio': bio})