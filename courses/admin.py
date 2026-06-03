from django.contrib import admin
from .models import Course, Enrollment, Lesson, Progress, Analytics

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Progress)
admin.site.register(Analytics)