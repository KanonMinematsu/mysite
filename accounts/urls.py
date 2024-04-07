from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('accounts_index', views.index, name='accounts_index'),
    path('create', views.create, name='create'),
    path('success', views.success, name='success'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),



]


