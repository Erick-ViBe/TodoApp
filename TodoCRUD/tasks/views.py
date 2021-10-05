from django import forms
from django.shortcuts import redirect, render, reverse, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskModelForm, TaskUpdateForm

# Create your views here.
def home_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/home.html', context)

def create_task_view(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            #description = form.cleaned_data['description']
            #Task.objects.create(description=description)
            task = form.save(commit=False)
            task.save()
            return redirect(reverse('home-view'))
    else:
        form = TaskModelForm()
    return render(request, 'tasks/create_form_task.html', {'form': form})  

def detail_form_task_view(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        if 'saveTask' in request.POST:
            form = TaskUpdateForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
        if 'deleteTask' in request.POST:
            task.delete()
        return redirect(reverse('home-view'))
    else:
        form = TaskUpdateForm(instance=task)
    
    return render(request, 'tasks/detail_form_task.html', {'form': form})