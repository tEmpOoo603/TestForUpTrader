from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('articles/', views.articles, name='articles'),
    path('news/', views.news, name='news'),
    path('news/2022', views.news_2022, name='news/2022'),
    path('news/2022/bad', views.news_2022_bad, name='news/2022/bad'),
    path('news/2022/good', views.news_2022_good, name='news/2022/good'),
    path('news/2023', views.news_2023, name='news/2023'),
    path('news/2023/bad', views.news_2023_bad, name='news/2023/bad'),
    path('news/2023/good', views.news_2023_good, name='news/2023/good'),
]
