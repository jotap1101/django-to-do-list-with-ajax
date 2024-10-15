from app.views import *
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', index, name='index'),
    path('task/create/', create_task, name='create_task'),
    path('task/<int:pk>/read/', read_task, name='read_task'),
    path('task/<int:pk>/update/', update_task, name='update_task'),
    path('task/<int:pk>/delete/', delete_task, name='delete_task'),
    path('task/filter/', filter_task, name='filter_task'),
]