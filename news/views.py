from django.shortcuts import render
from .models import News

def news(request):
    latest_news = News.objects.all().order_by('-published_date')[:5]  # 最新5件を取得
    return render(request, 'home/home.html', {'latest_news': latest_news})
