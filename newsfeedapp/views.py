from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import requests


API_KEY = '1dddff4a40694624917ef6388a945af7'


# Create your views here.
def articles_home (request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']
    
    context = {
        'articles' : articles
    }

    return render(request, 'newsfeedapp/articles_home.html', context)

def articles_home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    language = request.GET.get('language')

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?country={language}&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context = {
        'articles': articles
    }

    return render(request, 'newsfeedapp/articles_home.html', context)

def home(request):

    return render(request, 'newsfeedapp/home.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid details. Please check your input.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'newsfeedapp/login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have successfully registered and logged in.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'newsfeedapp/register.html', {'form': form})