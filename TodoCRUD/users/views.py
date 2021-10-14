from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserForm

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
