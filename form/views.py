from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
class ContactView(FormView):
    template_name = 'contact.html'
    success_url = '/'#どこにリダイレクトさせるか
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        # メール送信などを行う
        print(name, email, subject, message)
        return super().form_valid(form)#親クラスオーバーライド