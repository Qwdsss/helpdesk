from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='home'),
    path('problems/', views.problem_list, name='problem_list'),
    path('create_problem/', views.create_problem, name='create_problem'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
]
