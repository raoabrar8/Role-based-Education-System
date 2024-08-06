from django.urls import path
from .views import *


urlpatterns = [
    path('create_teacher_account/', create_teacher_account, name='create_teacher_account'),
    path('login/', LoginView, name='login'),
    path('myadmin/', AdminDashboard, name='dashboard'),
    path('logout/', LogoutView, name='logout'),
    path('', home, name='Home'),
    path('Teacher_login/', TeacherLoginView, name='Teacher_login'),
    path('student_login/', StudentLoginView, name='Student_login'),
    path('Student_portal', StudentPortal, name='student_portal'),
    path('Teacher_portal', TeacherPortal, name='Teacher_portal'),
    path('create_class/', Creat_class, name='create_class'),
    path('update_class/<int:id>/', Update_class, name='update_class'),
    path('delete_class/<int:id>/', Delete_class, name='delete_class'),
    path('create_lesson', Creat_lesson, name='create_lesson'),
    path('update_lesson/<int:id>/', Update_lesson, name='update_lesson'),
    path('delete_lesson/<int:id>/', Delete_lesson, name='delete_lesson'),
    path('create_quiz', Creat_quiz, name='create_quiz'),
    path('update_quiz/<int:id>', Update_quiz, name='update_quiz'),
    path('delete_quiz/<int:id>', Delete_quiz, name='delete_quiz'),
    path('check_result', check_result, name='check_result'),
    path('class_details/<int:id>/', Class_deatils, name='class_detail'),
    path('attempt_question/<int:question_id>', attempt_question, name='attempt_question' ),
    path('assign_class', Assign_class, name='assign_class'),
    path('question_list/', Question_list, name='question_list'),
    path('recent_result', Recent_result, name='recent_results')
    # path('add_student/', Add_student, name='add_student')
]
