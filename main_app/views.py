from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import *
from .forms import *
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

# Admin Views
def is_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(is_admin)
def AdminDashboard(request):
    return render(request, 'Accounts/Dashboard.html')


@user_passes_test(is_admin)
def create_teacher_account(request):
    if request.method == 'POST':
        form = TeacherRegistartionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_teacher = True
            user.save()
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            send_mail(
                'Yuour account has been created',
                f'Your Password is: {password}',
                [user.email]
            )
            return redirect('dashboard')
    else:
        form = TeacherRegistartionForm()
        
    return render(request, 'Accounts/Create_teacher_account.html', {'form' : form})



def LoginView(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
            else:
                message = "Credential error"
        except User.DoesNotExist:
            message = 'User doesnot exist'
            
    return render(request, 'Accounts/Admin_login.html', {'message': message})



# Student views
def StudentLoginView(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_student:
                    login(request, user)
                    return redirect('student_portal')
            else:
                message = "Credential error"
        except User.DoesNotExist:
            message = 'User doesnot exist'
            
    return render(request, 'Student/Student_login.html', {'message': message})


def StudentPortal(request):
    
    return render(request, 'Student/Student_portal.html')


def attempt_question(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        given_answer = request.POST.get('answer')
        correct_answer = question.answer_set.first().correct_answer
        score = 10 if given_answer == correct_answer else 0
        return render(request, 'Student/student_result.html', {'score': score})
    return render(request, 'Student/Attempt_quiz.html', {'question': question})

def Question_list(request):
    questions = Question.objects.all()
    return render(request, 'Student/Question_list.html', {'questions' : questions})

def Recent_result(request):
    return render(request, 'Student/Recent_result.html')

# def Student_result(request):
#     return render(request, 'Student/student_result.html')

def Check_results(request, id):
    answer = get_object_or_404(Question, id=id)
    return render(request, 'Student/Check_results.html', {'answer':answer}) 



# Home view
def home(request):
    return render(request, 'Accounts/Home.html')




# Teacher View
def TeacherLoginView(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_teacher:
                    login(request, user)
                    return redirect('Teacher_portal')
            else:
                message = "Credential error"
        except User.DoesNotExist:
            message = 'User doesnot exist'
            
    return render(request, 'Teacher/Teacher_login.html', {'message': message})

def TeacherPortal(request):
    classes = Class.objects.all()
    Quizez =Question.objects.all()
    Lessons = Lesson.objects.all()
    context = {'classes':classes, 'Quizez':Quizez, 'Lessons': Lessons}
    return render(request, 'Teacher/Teacher_portal.html', context)


def Assign_class(request):
    if request.method == 'POST':
        Aform = AssignClassForm(request.POST)
        if Aform.is_valid():
            Aform.save()
            return redirect('Teacher_portal')
    else:
        Aform = AssignClassForm()
    return render(request, 'Teacher/Assign_class.html', {'Aform':Aform})


def Creat_class(request):
    if request.method == 'POST':
        Cform = ClassForm(request.POST)
        if Cform.is_valid():
            class_obj = Cform.save(commit=False)
            class_obj.teacher = Teacher.objects.get(user=request.user)
            class_obj.save()
            return redirect('Teacher_portal')
    else:
        Cform = ClassForm()
    return render(request, 'Teacher/Create_class.html', {'Cform':Cform})



def Update_class(request, id):
    classes = get_object_or_404(Class, id=id)
    if request.method == 'POST':
        Cform = ClassForm(request.POST, instance=classes)
        if Cform.is_valid():
            Cform.save()
            return redirect('Teacher_portal')
    else:
        Cform = ClassForm(instance=classes)
    return render(request, 'Teacher/update_class.html', {'Cform':Cform})

def Delete_class(request, id):
    classes = get_object_or_404(Class, id=id)
    classes.delete()
    return redirect('Teacher_portal')
    
# Lesson Views   
def Creat_lesson(request):
    if request.method == 'POST':
        Lform = LessonForm(request.POST)
        if Lform.is_valid():
            Lform.save()
            return redirect('Teacher_portal')
    else:
        Lform = LessonForm()
    return render(request, 'Teacher/Create_lesson.html', {'Lform':Lform})

def Update_lesson(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    if request.method == 'POST':
        Lform = LessonForm(request.POST, instance=lesson)
        if Lform.is_valid():
            Lform.save()
            return redirect('Teacher_portal')
    else:
        Lform = LessonForm(instance=lesson)
    return render(request, 'Teacher/update_lesson.html', {'Lform':Lform})

def Delete_lesson(request, id):
    Lesson = get_object_or_404(Lesson, id=id)
    Lesson.delete()
    return redirect('Teacher_portal')


# quiz views

def Creat_quiz(request):
    if request.method == 'POST':
        Qform = QuestionForm(request.POST)
        if Qform.is_valid():
            Qform.save()
            return redirect('Teacher_portal')
    else:
        Qform = QuestionForm()
    return render(request, 'Teacher/Create_quiz.html', {'Qform':Qform})

def Update_quiz(request, id):
    quiz = get_object_or_404(Question, id=id)
    if request.method == 'POST':
        Qform = QuestionForm(request.POST, instance=quiz)
        if Qform.is_valid():
            Qform.save()
            return redirect('Teacher_portal')
    else:
        Qform = QuestionForm(instance=quiz)
    return render(request, 'Teacher/update_lesson.html', {'Qform':Qform})

def Delete_quiz(request, id):
    quiz = get_object_or_404(Question, id=id)
    quiz.delete()
    return redirect('Teacher_portal') 


def check_result(request):
    return render(request, 'Teacher/Check_student_results.html')


def Class_deatils(request, id):
    classes = get_object_or_404(Class, id=id)
    lessons = classes.lessons.all()
    questions = Question.objects.filter(lesson__in=classes.lessons.all())
    context = {'classes':classes, 'lessons': lessons, 'questions':questions}
    return render(request, 'Teacher/Class_detail.html', context)


# logout view
def LogoutView(request):
    logout(request)
    return redirect('Home')