from django.urls import path
from . import views

urlappterns = [
    path('login/', views.user_login, name='login')
]