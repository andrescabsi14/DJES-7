from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #Lessons
    url(r'^lessons/(?P<title>[\w\-]+)/', 'lessons.views.lesson_view', name='lesson_view'),
	#Signup
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    #SignIn
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),

)
