import requests

def get_instagram_posts():
    access_token = 'EAAWP0w6t9cMBO2ZCAHEkZA0FE42ZBOivvzr5QYnP2Tr1GXBRU5ZBtUb3KOjUkZAnZBV7f6AMcoeAC0NmxhTyJfiTWDAXPVZCMo2YBeb42BaBaYNnFrTkuBkcnXBnTF0BDOYw3ggttkrs6SFQemsDU1ndBWpHNTz0D5wLLfoqb7orCfRFFNFKYvWzQEgSuXoRgZDZD'
    user_id = '282372828964318'
    url = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url&access_token={access_token}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None
