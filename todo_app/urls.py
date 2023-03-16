from django.urls import path 
from .views import create_todo, update_todo, get_todos, delete_todo, get_todo


urlpatterns = [
    path('todos/<int:pk>/', get_todos),
    path('todos/', get_todos),
    path('create-todo/', create_todo),
    path('delete-todo/<int:pk>/', delete_todo),
    path('update-todo/<int:pk>/', update_todo),
    path('todo/<int:pk>/', get_todo)
]