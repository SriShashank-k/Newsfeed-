from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('article/',views.articles_home,name = 'articles')
]