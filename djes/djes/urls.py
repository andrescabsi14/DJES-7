from django.conf.urls import patterns, include, url
from django.conf import settings
from lessons.views import LessonDetailView, LessonListView
from django.contrib import admin
admin.autodiscover()
from rest_framework import routers



#API REST
from lessons.views import LessonViewSet
router = routers.DefaultRouter()
router.register(r'lessons', LessonViewSet)


#URLS
urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),


    # url(r'^$', 'home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls')),
    #Lessons
    #url(r'^lessons/(?P<title>[\w\-]+)/', 'lessons.views.lesson_view', name='lesson_view'),
    url(r'^lessons/(?P<pk>[\d]+)', LessonDetailView.as_view()),
    url(r'^lessons/', LessonListView.as_view()),
	#Signup
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    #SignIn
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),

    #API REST
    url(r'^api/', include(router.urls)),

)

