""" views module """
from django.shortcuts import render
from .forms import TasksForm
from django.shortcuts import redirect

def index(request):
    """ index view """
    return render(request, 'todo/index.html')

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
