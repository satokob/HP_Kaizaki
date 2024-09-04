import requests
from django.shortcuts import render
from news.models import News  

def get_instagram_posts():
    access_token = 'IGQWRONjNkTHhMRWVFeTZAONm8ySjVDeVphVmJwMDM4QUxMYnFlZAWVXLXRqUG9GWUdNaERtcF9vWUsxemtuUWVpU3k0S2J4YWxOVWN2UmQxRjIzRE9FMjdRZAkIyaTRBRmNjZA1FnOW9JUVdLdU9xYXNpeDFWUmowNFkZD'
    user_id = '17841407386127966'
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
