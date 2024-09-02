import requests
from django.shortcuts import render

def get_instagram_posts():
    access_token = 'IGQWRONjNkTHhMRWVFeTZAONm8ySjVDeVphVmJwMDM4QUxMYnFlZAWVXLXRqUG9GWUdNaERtcF9vWUsxemtuUWVpU3k0S2J4YWxOVWN2UmQxRjIzRE9FMjdRZAkIyaTRBRmNjZA1FnOW9JUVdLdU9xYXNpeDFWUmowNFkZD'  # Instagram APIのアクセストークン
    user_id = '17841407386127966'  # InstagramのユーザーID
    url = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp&access_token={access_token}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def home(request):
    instagram_posts = get_instagram_posts()
    return render(request, 'home.html', {'instagram_posts': instagram_posts})