from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='名前', required=True)
    email = forms.EmailField(label='メールアドレス', required=True)
    subject = forms.CharField(label='件名', required=True)
    message = forms.CharField(label='メッセージ', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'name'
        self.fields['email'].widget.attrs['placeholder'] = 'mail'
        self.fields['subject'].widget.attrs['placeholder'] = 'subject'
        self.fields['message'].widget.attrs['placeholder'] = 'message'
   