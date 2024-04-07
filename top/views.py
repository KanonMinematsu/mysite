from django.http import HttpResponse 
from django.template import loader 

def index(request):
    template = loader.get_template("top/index.html")
    return HttpResponse(template.render({}, request))

def index2(request):
    template = loader.get_template("top/news.html")
    return HttpResponse(template.render({}, request))

from django.views.generic import FormView
from .forms import ContactForm
class ContactView(FormView):
    template_name = 'form/contact.html'
    success_url = '/'#どこにリダイレクトさせるか
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # メール送信などを行う
        print(name, email, message)
        return super().form_valid(form)#親クラスオーバーライド
