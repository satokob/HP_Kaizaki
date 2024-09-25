import requests

def get_instagram_posts():
    access_token = 'EAAWP0w6t9cMBO2ZCAHEkZA0FE42ZBOivvzr5QYnP2Tr1GXBRU5ZBtUb3KOjUkZAnZBV7f6AMcoeAC0NmxhTyJfiTWDAXPVZCMo2YBeb42BaBaYNnFrTkuBkcnXBnTF0BDOYw3ggttkrs6SFQemsDU1ndBWpHNTz0D5wLLfoqb7orCfRFFNFKYvWzQEgSuXoRgZDZD'
    business_account_id = '17841407386127966'
    url = f'https://graph.facebook.com/v20.0/{business_account_id}/media?fields=id,caption,media_type,media_url,permalink,timestamp,username&access_token={access_token}'

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['data']
    else:
        return None
