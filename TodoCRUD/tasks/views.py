from django import forms
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, TaskModelForm, TaskUpdateForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class HomeClassListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        #tasks = Task.objects.filter(user=self.request.user)
        tasks = self.request.user.tasks.all()
        return tasks


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create_form_task.html'
    form_class = TaskModelForm
    success_url = '/'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DetailTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/detail_form_task.html'
    success_url = '/'


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'