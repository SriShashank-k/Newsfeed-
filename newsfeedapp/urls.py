from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('articles/', views.articles_home, name='articles'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('articles/', views.articles_home, name='articles_home'),
    path('headlines/', views.headline_list, name='headline_list'),
    path('headlines/<int:headline_id>/reviews/', views.headline_reviews, name='headline_reviews'),
    path('delete_review/', views.delete_review, name='delete_review'),
]