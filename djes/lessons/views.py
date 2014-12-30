from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

#Create your views here
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Lesson

def lesson_view(request, title):
	##Return 404 if not exist
	lesson = get_object_or_404(Lesson, title=title)
	##Custom Variables for view
	bio = lesson.teacher.profile
	##Return lesson if exist
	return render(request, 'lessons/lesson.html', {'lesson': lesson, 'bio': bio})


class LessonListView(ListView):
	model = Lesson
	context_object_name = 'lessons'
	template_name = 'lessons/lessons.html'
	def get_context_data(self, **kwargs):
		context = super(LessonListView, self).get_context_data(**kwargs)
		is_auth = False

		if self.request.user.is_authenticated():
			is_auth = True

		context.update({'is_auth': is_auth})
		return context


class LessonDetailView(DetailView):
	model = Lesson
	context_object_name = 'lesson'
	template_name = 'lessons/lesson.html'

#API REST
from rest_framework import viewsets

class LessonViewSet(viewsets.ModelViewSet):
	model = Lesson