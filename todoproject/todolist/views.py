from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, RegisterForm
from django.contrib.auth import authenticate, login

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todolist/index.html',{'tasks':tasks})

@login_required
def taskdetail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'todolist/task_detail.html', {'task': task})

@login_required
def taskcreate(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request, 'todolist/task_create.html', {'form': form, 'update': False})

@login_required
def taskupdate(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todolist/task_create.html',{'form': form, 'update': True }) 

@login_required
def taskdelete(request, task_id):
    task = get_object_or_404(Task, id=task_id) 
    if request.method == "POST":
        task.delete()
        return redirect('home')
    return render(request, 'todolist/task_create.html', {'task': task})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "todolist/register.html", {"form": form})

