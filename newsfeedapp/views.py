from django.shortcuts import render
import requests
API_KEY = '1dddff4a40694624917ef6388a945af7'


# Create your views here.
def home (request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']
    
    context = {
        'articles' : articles
    }

    return render(request, 'news_api/home.html', context)