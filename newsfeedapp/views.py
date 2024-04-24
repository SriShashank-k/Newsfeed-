from django.shortcuts import render
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