from django.urls import path
from .views import HomeClassListView, CreateTaskView, DetailTaskView, DeleteTaskView

urlpatterns = [
    path('', HomeClassListView.as_view(), name='home-view'),
    path('crear/', CreateTaskView.as_view(), name='create_task'),
    path('tarea/<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
    path('tarea/delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task')
]