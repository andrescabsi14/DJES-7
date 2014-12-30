from django.conf import settings
from django.conf.urls import patterns, include, url


from commercial.views import HomeView, LoginView
from lessons.views import LessonDetailView, LessonListView


from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()
from rest_framework import routers



#API REST
from lessons.views import LessonViewSet
router = routers.DefaultRouter()
router.register(r'lessons', LessonViewSet)


#URLS
urlpatterns = patterns('',

    #Home
    url(r'^$', HomeView.as_view()),
    #Login
    url(r'^ingresar/', LoginView.as_view()),
    #Admin
    url(r'^admin/', include(admin.site.urls)),
    #Courses
    url(r'^courses/', include('courses.urls')),
    #Lessons
    #url(r'^lessons/', LessonListView.as_view(), name='lessons'),
    #url(r'^lessons/(?P<title>[\w\-]+)/', LessonDetailView.as_view(), name='lesson'),
	#Signup
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    #SignIn
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),

    #API REST
    url(r'^api/', include(router.urls)),

)

