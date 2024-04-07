from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login, logout

def top(request):
    return render(request, 'top.html')


def index(request):
    context = {'user':request.user}
    return render(request, 'login.html', context)

def create(request):
    return render(request, 'create.html')

def success(request):
    return render(request, 'success.html')


def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(username=username, password=password)
    new_user.save()
    return render(request, 'success.html')

def signin(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('ログインに失敗しました')
    
    if user.password == password:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('ログインに失敗しました')
    
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')




