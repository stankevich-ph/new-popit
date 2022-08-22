from django.urls import path

from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('rating', views.rating_view, name='rating_view'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:id>/delete', views.NewsDeleteView, name='news-delete'),
    path('<int:news_id>/like_action/', views.LikeAction.as_view(), name='like_action'),
]
