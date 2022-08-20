from django.urls import path
from . import views
from django.contrib import admin
from .views import *
urlpatterns = [
    path('', add_user_settings.as_view(), name='user_profile'),
    path('<int:id>/edit', views.UpdateUserInformation, name='userupdate'),
    path('photographers', views.photographers_view, name='photographers'),
]