from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('articles/', views.articles_home, name='articles'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
]