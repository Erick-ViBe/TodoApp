from django import forms
from django.shortcuts import redirect, render, reverse
from .models import Task
from .forms import TaskForm, TaskModelForm

# Create your views here.
def home_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/home.html', context)

def create_task_view(request):
    if request.POST:
        new_task = request.POST.get('task')
        Task.objects.create(description=new_task)
        return redirect(reverse('home-view'))
    
    return render(request, 'tasks/create_task.html')

def detail_task_view(request, pk):
    task = Task.objects.get(id=pk)

    if request.POST:
        if 'saveTask' in request.POST:
            new_description = request.POST.get('task_description')
            new_done = request.POST.get('task_done')
            if new_done == 'on':
                new_done = True
            else:
                new_done = False
            task.description = new_description
            task.done = new_done
            task.save()
            
        if 'deleteTask' in request.POST:
            task.delete()

        return redirect(reverse('home-view'))

    context = {
        'task': task
    }
    return render(request, 'tasks/detail_task.html', context)

def create_form_task_view(request):
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