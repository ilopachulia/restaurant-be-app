
from django.urls import path
from user import views

urlpatterns = [
    path('registration/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
]
