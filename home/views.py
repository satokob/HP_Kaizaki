import requests
from django.shortcuts import render
from news.models import News  

def get_instagram_posts():
    access_token = 'EAAWP0w6t9cMBOZCUCC4CzZAJ8Al2l5rh8md5O23ccrNYw9H9XeiDPwRCHQ3ZAFUBxZAVUvHZBGJOq1RQt6ZCb9FgVAkKZBhlT6yGDVZBlKpcxxMZBbgUYZABVShteTASGFVS7lBfeeCshCYF9TknstsfG01JxZATb3uKHIQUQNj0w41gGOnWyhYnZCuufydbv5sdKQZDZD'
    user_id = '181475575221097'
    url = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp&access_token={access_token}'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def home(request):
    instagram_posts = get_instagram_posts()
    latest_news = News.objects.all().order_by('-published_date')[:5]  
    return render(request, 'home/home.html', {
        'instagram_posts': instagram_posts,
        'latest_news': latest_news  # ニュースをテンプレートに渡す
    })
