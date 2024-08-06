from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Teacher, Student, Class, Lesson, Question, Answer, StudentClass

class TeacherRegistartionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user']



# teacher Forms

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'class_obj']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['lesson', 'question_text', 'question_type', 'question_answer']
        
# Student forms

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['correct_answer']
        
        
class AssignClassForm(forms.ModelForm):
    class Meta:
        model = StudentClass
        fields = ['student', 'class_obj']
        