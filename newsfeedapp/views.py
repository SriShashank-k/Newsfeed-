from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import requests
from django.shortcuts import render, redirect, get_object_or_404
from .models import Headline, Review
from django.contrib.auth.decorators import login_required

#API_KEY = '1dddff4a40694624917ef6388a945af7'


# Create your views here.
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Headline

def articles_home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    language = request.GET.get('language')
    API_KEY = '1dddff4a40694624917ef6388a945af7'  # Replace 'YOUR_NEWSAPI_KEY' with your actual NewsAPI key

    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    elif category:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?language={language}&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])  # Extract articles from the API response

    # Save fetched headlines to the database
    # Save fetched headlines to the database with country tag
    for article in articles:
        new_headline = Headline(
            title=article['title'],
            description=article['description'],
            url=article['url'],
            source_name=article['source']['name'],
            published_at=article['publishedAt'],
            country=country,  # Save country tag
            category=category,  # Save category tag
            language=language  # Save language tag
        )                
        new_headline.save()


    # Fetch headlines from the database based on the specified filters
    if country:
        headlines = Headline.objects.filter(country=country)
    elif category:
        headlines = Headline.objects.filter(category=category.lower())
    elif language:
        headlines = Headline.objects.filter(language=language)
    else:
        headlines = Headline.objects.all()

    context = {
        'headlines': headlines
    }

    return render(request, 'newsfeedapp/articles_home.html', context)
def headline_reviews(request, headline_id):
    headline = get_object_or_404(Headline, pk=headline_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_content = form.cleaned_data['review']
            # Create a new review associated with the headline
            Review.objects.create(headline=headline, review=review_content, user=request.user)
            return redirect('headline_reviews', headline_id=headline_id)
    else:
        form = ReviewForm()

    # Fetch all reviews for the headline
    reviews = Review.objects.filter(headline=headline)

    context = {
        'headline': headline,
        'form': form,
        'reviews': reviews
    }

    return render(request, 'newsfeedapp/headline_reviews.html', context)

@login_required
def delete_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, pk=review_id)

        # Check if the review belongs to the current user
        if review.user == request.user:
            review.delete()

    return redirect('headline_reviews', headline_id=review.headline.id)

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

def headline_list(request):
    # Fetch the query parameters from the request
    country = request.GET.get('country')
    category = request.GET.get('category')
    language = request.GET.get('language')

    # Initialize the queryset with all Headline objects
    headlines = Headline.objects.all()

    if country:
        headlines = headlines.filter(country=country)
    if category:
        headlines = headlines.filter(category=category)
    if language:
        headlines = headlines.filter(language=language)
    # Render the template with the filtered queryset
    return render(request, 'newsfeedapp/headline_list.html', {'headlines': headlines})