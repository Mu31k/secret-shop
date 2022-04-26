from django.urls import path
from django.urls import re_path
from . import views

# app_name = 'polls'
urlpatterns = [
    path('', views.index, name='home'),
    path('sign', views.sign, name='sign'),
    path('news', views.sign),
    path('discount/?page=<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),]

# ]<slug:pk>