from django.shortcuts import render, get_object_or_404

from Home.models import MenuItem


def home(request):
    return render(request,'Home/home.html')

def about(request):
    return render(request,'Home/about.html')

def feedback(request):
    return render(request,'Home/feedback.html')

def articles(request):
    return render(request,'Home/articles.html')

def news(request):
    return render(request,'Home/news.html')

def year_news(request, year):
    year_news = get_object_or_404(MenuItem, name=year)
    return render(request,'Home/year_news.html')
