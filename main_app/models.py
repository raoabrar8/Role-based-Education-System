from django.contrib.auth.models import AbstractUser
from django.db import models


# Role models
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

# teacher models
class Class(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    
    def __str__(self):
        return self.title

class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    QUESTION_TYPES = (
        ('FB', 'Fill in the blanks'),
        ('TF', 'True/False'),
        ('MC', 'Multiple Choice'),
    )
    question_type = models.CharField(max_length=100, choices=QUESTION_TYPES)
    question_answer = models.CharField(max_length=254)
    
    def __str__(self):
        return self.question_text
    
    
    
class StudentClass(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_class')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)
    
# Student models
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=254)
    
    def __str__(self):
        return self.correct_answer


