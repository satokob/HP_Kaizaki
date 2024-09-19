import requests

def get_instagram_posts():
    access_token = 'EAAWP0w6t9cMBO4yP2FYnFUO2xpAOZBZCj77RYEraI8Mm7a0w2befJRSjtT7eeSxRKhGHjrUsYmFHaZBAHvSvc7r9JSEF283U0ZBHQMJJf9YepbXtUBpvjzXNubrE2zJyHtvBkW0eXZB0pL82sVlZAL0ngGCIdZAkHEStOePZBZAv1ZBYKwCEIMi7ekARZAZBi6vQMgZDZD'
    user_id = '181475575221097'
    url = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url&access_token={access_token}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None
