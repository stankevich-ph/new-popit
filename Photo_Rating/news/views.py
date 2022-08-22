from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, UpdateView, View
from django.http.response import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User
from django.db.models import Count

from .models import Articles, Like
from .forms import ArticlesForm


def news_home(request):
    if request.method == "POST":
        comments = Articles.objects.comments(id=id)
        comments.comments = request.POST['comments']
        comments.save()
    else:
        news = Articles.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True)
        ).order_by('-data')

        sites = 'news/news_home.html'
        return render(request, sites, {'news': news, 'user': auth.get_user(request)})


class LikeAction(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Авторизуйтесь, чтобы ставить лайки.")

        article_id = kwargs["id"]
        try:
            like = Like.objects.get(article_id=article_id, user_id=request.user.id)
            like.delete()
            return HttpResponse("0")
        except Like.DoesNotExist:
            Like.objects.create(article_id=article_id, user=request.user)
            return HttpResponse("1")


class AddComment(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Авторизуйтесь, чтобы оставлять комментарии.")

        article = get_object_or_404(Articles, pk=kwargs['id'])
        article.comments.create(user_id=request.user.id, content=request.POST.get('comment'))

        return redirect("news_home")


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/update_news.html'
    form_class = ArticlesForm


def news_delete_view(requests, pk):
    model = Articles.objects.get(id=pk)
    model.delete()
    return redirect('news_home')


def create(request):
    user_name = auth.get_user(request).username
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = User.objects.get(username=user_name)
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не корректна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def rating_view(request):
    news = Articles.objects.annotate(likes_count=Count('likes', distinct=True)).order_by('-likes_count')
    sites = 'news/news_rating.html'
    return render(request, sites, {'news': news, 'user': auth.get_user(request)})

