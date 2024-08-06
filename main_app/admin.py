from django.contrib import admin
from .models import User, Teacher, Student, Class, Lesson, Question, Answer, StudentClass
from django.contrib.auth.admin import UserAdmin





admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(StudentClass)
