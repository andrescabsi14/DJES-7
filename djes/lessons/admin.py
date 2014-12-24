from django.contrib import admin

from .models import Lesson

class TrackAdmin(admin.ModelAdmin):
	#List View Attr of model
	list_display = ('order', 'image', 'title', 'teacher', 'course')
	#List Filter Attr of model
	list_filter = ('teacher', 'course')
	#Search
	search_fields = ('title', 'teacher__first_name')
admin.site.register(Lesson, TrackAdmin)