from django.urls import path
from .views import login_view, logout_view, TodoLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TodoLoginView.as_view(), name='login-view'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    #path('404_not_found/', NotFound404.as_view(), name='404-view')
]