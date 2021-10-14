from django import forms
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm, TaskModelForm, TaskUpdateForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView


class HomeClassListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/home.html'
    context_object_name = 'tasks'


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create_form_task.html'
    form_class = TaskModelForm
    success_url = '/'


class DetailTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/detail_form_task.html'
    success_url = '/'