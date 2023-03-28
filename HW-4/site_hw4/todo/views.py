from django.db.models.fields import BigAutoField
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import TaskModel
from .forms import TaskForm

# Renders all the available tasks
def make_views(request):
    # Create a new task if the request to this page was a POST
    if request.method == 'POST':
        newtask = TaskModel()
        newtask.task = request.POST['task']
        if newtask.task != "":
            newtask.created = timezone.localtime()
            newtask.completed = False
            newtask.save()

    tasks = TaskModel.objects.all()
    # The names of the task fields
    #fieldnames = [k for k,_ in TaskModel.__dict__.items() if not "__" in k]
    #fieldnames = [f.name for f in TaskModel._meta.fields]

    context = { 'tasks': tasks }
    return render(request, 'todo/index.htmlx', context)

def complete_task(request, id):
    comptask = TaskModel.objects.get(id=id)
    comptask.completed = True
    comptask.save()
    return redirect('todo_index')

def update_task(request, id):
    task = TaskModel.objects.get(id=id)

    if request.method != 'POST':
        form = TaskForm(instance=task)
        context = { 'task':task, 'form':form }
        return render(request, 'todo/update.htmlx', context)

    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save().save()

    return redirect('todo_index')

def delete_view(request, id):
    task = TaskModel.objects.get(id=id)

    context = { 'task':task }
    return render(request, 'todo/delete.htmlx', context)

def delete_task(request, id):
    task = TaskModel.objects.get(id=id)
    task.delete()
    return redirect('todo_index')
