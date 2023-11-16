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

def news_2022(request):
    return render(request, 'Home/news_2022.html')
def news_2022_bad(request):
    return render(request, 'Home/news_2022_bad.html')
def news_2022_good(request):
    return render(request, 'Home/news_2022_good.html')

def news_2023(request):
    return render(request, 'Home/news_2023.html')
def news_2023_bad(request):
    return render(request, 'Home/news_2023_bad.html')
def news_2023_good(request):
    return render(request, 'Home/news_2023_good.html')




