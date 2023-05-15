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
