from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User


def news_home (request):
    if request.method == "POST":
        news = Articles.objects.order_by('-data')
        comments = Articles.objects.comments (id=id)
        comments.comments = request.POST['comments']
        comments.save()
    else:
        news = Articles.objects.order_by('-data')
        comments = Articles.objects.all()
        sites = 'news/news_home.html'
        return render(request, sites, {'news': news, 'comments': comments , 'user':auth.get_user(request)})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update_news.html'
    form_class = ArticlesForm

def NewsDeleteView(requests, id):
    model = Articles.objects.get(id=id)
    model.delete()
    return redirect('news_home')

def create (request):
    user_name = auth.get_user(request).username
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = User.objects.get(username = user_name)
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не корретна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

def rating_view (request):
    if request.method == "POST":
        news = Articles.objects.order_by('-like')
    else:
        news = Articles.objects.order_by('-like')
    sites = 'news/news_rating.html'
    return render(request, sites, {'news': news, 'user': auth.get_user(request)})

