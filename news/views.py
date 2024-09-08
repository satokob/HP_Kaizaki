from django.urls import path
from django.shortcuts import render
from .models import News  

# news関数を定義
def news(request):
    latest_news = News.objects.all().order_by('-published_date')[:5]  # 最新5件を取得
    return render(request, 'news/news.html', {'latest_news': latest_news})  

# URLパターンを定義
urlpatterns = [
    path('', news, name='news'),  
]
