from django.contrib import admin
from .models import Articles, Comment, Like

admin.site.register(Articles)
admin.site.register(Comment)
admin.site.register(Like)
