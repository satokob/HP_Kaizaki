from django import forms

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
