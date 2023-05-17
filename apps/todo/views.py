""" views module """
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TasksForm
from .models import Tasks


def index(request):
    """ index view """
    tasks = Tasks.objects.all().order_by('-created_at')
    context = {'tasks': tasks}
    return render(request, 'todo/index.html', context)


def create(request):
    """ create view """
    form = TasksForm()
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'todo/create.html', context)

def details(request, pk):
    """ detail view"""
    task = Tasks.objects.get(id = pk)
    context = {'task': task}
    return render(request, 'todo/view.html', context)

def edit(request, pk):
    """ edit view """
    task = Tasks.objects.get(id = pk)
    form = TasksForm(instance=task)
    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'todo/edit.html', context)

def remove(request, pk):
    """ delete view """
    task = Tasks.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
        
    context = {'task': task}
    return render(request, 'todo/delete.html', context)