from django.urls import path

from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('rating', views.rating_view, name='rating_view'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:id>/delete', views.news_delete_view, name='news-delete'),
    path('<int:id>/add_comment/', views.AddComment.as_view(), name='add_comment'),
    path('<int:id>/like_action/', views.LikeAction.as_view(), name='like_action'),
]
