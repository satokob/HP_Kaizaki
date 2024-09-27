import requests
from django.shortcuts import render
from news.models import News  
from .instagram_api import get_instagram_posts 

def home(request):
    instagram_posts = get_instagram_posts()
    latest_news = News.objects.all().order_by('-published_date')[:5]  
    return render(request, 'home/home.html', {
        'instagram_posts': instagram_posts,
        'latest_news': latest_news  # ニュースをテンプレートに渡す
    })

def gallery(request):
  instagram_posts = get_instagram_posts()
  return render(request, 'home/home.html', {'instagram_posts': instagram_posts})
