import requests

def get_instagram_posts(max_items=6):
    access_token = 'EAAWP0w6t9cMBO2ZCAHEkZA0FE42ZBOivvzr5QYnP2Tr1GXBRU5ZBtUb3KOjUkZAnZBV7f6AMcoeAC0NmxhTyJfiTWDAXPVZCMo2YBeb42BaBaYNnFrTkuBkcnXBnTF0BDOYw3ggttkrs6SFQemsDU1ndBWpHNTz0D5wLLfoqb7orCfRFFNFKYvWzQEgSuXoRgZDZD'
    business_account_id = '17841407386127966'
    url = f'https://graph.facebook.com/v20.0/{business_account_id}/media?fields=id,caption,media_type,media_url,permalink,timestamp,username&access_token={access_token}'

    media_list = []
    while len(media_list) < max_items:
        # APIリクエスト
        response = requests.get(url)
        if response.status_code != 200:
            return []

        data = response.json()

        # フィルタリングしてIMAGEかVIDEOのみ追加
        for media in data['data']:
            if media['media_type'] in ['IMAGE', 'VIDEO']:
                media_list.append(media)
                if len(media_list) >= max_items:
                    break

        # 次ページがある場合はpaging.nextを利用する
        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']
        else:
            break  # 次のページがない場合は終了

    return media_list[:max_items]
