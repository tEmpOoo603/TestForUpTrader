from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('articles/', views.articles, name='articles'),
    path('news/', views.news, name='news'),
    path('news/<int:year>/', views.year_news, name='year_news'),

]
