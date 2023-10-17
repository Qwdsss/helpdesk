from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem
from .forms import ProblemForm, ProblemDetailForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.models import Group


reception_group, created = Group.objects.get_or_create(name='Reception')
tester_group, created = Group.objects.get_or_create(name='Tester')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('problem_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def problem_list(request):
    problems = Problem.objects.exclude(status='resolved').filter(assigned_user=request.user)
    return render(request, 'problem_list.html', {'problems': problems})


def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.assigned_user = request.user
            problem.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'create_problem.html', {'form': form})


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)

    if request.method == 'POST':
        form = ProblemDetailForm(request.POST, instance=problem)
        if form.is_valid():
            form.save()
            return redirect('problem_list')
    else:
        form = ProblemDetailForm(instance=problem)

    return render(request, 'problem_detail.html', {'problem': problem, 'form': form})

