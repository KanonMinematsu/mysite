from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("news", views.index, name="index2"),
    path('contact', views.ContactView.as_view(), name='hhh')
]