from django import forms
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=50, error_messages={'required': '必須項目です'})
    kana = forms.CharField(label='ふりがな', max_length=50, error_messages={'required': '必須項目です'})
    email = forms.EmailField(label='メールアドレス', error_messages={
        'required': '必須項目です',
        'invalid': 'メールアドレスが適切ではありません'
    })
    phone = forms.CharField(label='お電話番号', required=False)  # 任意項目
    TITLE_CHOICES = [
        ('contact', 'ー お問い合わせ内容を選択してください ー'),
        ('wedding', 'ウェディング撮影のお見積もり依頼'),
        ('lesson', 'レッスンのご依頼'),
        ('other', 'その他のご質問'),
    ]
    title = forms.ChoiceField(label='タイトル', choices=TITLE_CHOICES, error_messages={'required': '必須項目です'})
    message = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea, required=False)

    # メールアドレスに '@' が含まれているか確認するカスタムバリデーション
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@' not in email:  # メールアドレスに '@' が含まれているかを確認
            raise forms.ValidationError('このメールアドレスは適切ではありません。')
        return email

    # 複数フィールドに基づいたカスタムバリデーション
    def clean(self):
        cleaned_data = super().clean()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')

        # 電話番号とメールアドレスが両方空の場合にエラーメッセージを出す
        if not phone and not email:
            raise forms.ValidationError('電話番号またはメールアドレスのいずれかを入力してください。')
    
    #メール送信設定
    def send_email(self):
        name = self.cleaned_data['name']
        kana = self.cleaned_data['kana']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        # メール内容の設定
        subject = f'[お問い合わせ] {title}'
        body = (
            f'webサイト経由でお問合せがありました。\n\n'
            f'送信者 : {name}\n'
            f'ふりがな : {kana}\n'
            f'メールアドレス : {email}\n'
            f'電話番号 : {phone}\n'
            f'メッセージ : {message}\n'
        )

        from_email = 'satoki.kob@gmail.com'
        to_list =['kaizakimaria@gmail.com']
        bcc_list = ['adao1994saru@yahoo.co.jp']

         # メール送信処理
        msg = EmailMessage(subject=subject, body=body, from_email=from_email, to=to_list, bcc=bcc_list)
        msg.send()