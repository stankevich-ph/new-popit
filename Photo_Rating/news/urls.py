from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('rating', views.rating_view, name='rating_view'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:id>/delete', views.NewsDeleteView, name='news-delete'),
]
