from django.shortcuts import render
from .models import Task

# Create your views here.
def home_view(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/home.html', context)