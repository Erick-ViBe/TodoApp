from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .forms import UserForm
from django.views.defaults import page_not_found

def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contraseña']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home-view'))
    else:
        form = UserForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('login-view'))


class TodoLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def not_found_404(request):
    template_name = 'users/404.html'
    return page_not_found(request, template_name=template_name)