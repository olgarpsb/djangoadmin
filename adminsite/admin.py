from django.contrib import admin
from .models import Course, Instructor, Lesson



class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]


#class CourseAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'name', 'description']

    # Register your models here.
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
