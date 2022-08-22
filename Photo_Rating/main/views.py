from django.shortcuts import render, redirect


def index(request):
     # return render(request, 'index/index.html')
     return redirect('news_home')


def auth(request):
     return render(request, 'main/Authorization.html')


def about(request):
     return render(request, 'main/about.html')

