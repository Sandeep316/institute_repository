from django.contrib import admin

from .models import CoursesData
class AdminCourseData(admin.ModelAdmin):
    list_display = ['course_id',
                    'course_name',
                    'course_dur',
                    'course_fee',
                    'course_date',
                    'course_time',
                    'trainer_name',
                    'trainer_exp']

admin.site.register(CoursesData,AdminCourseData)
