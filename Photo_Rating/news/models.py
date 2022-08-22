from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField('Название', max_length=80)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')
    image = models.ImageField(blank=True, upload_to='img/')
    image_url = models.ImageField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Like(models.Model):
    article = models.ForeignKey(Articles, verbose_name="Новость", related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=models.SET_NULL)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, blank=True)


class Comment(models.Model):
    article = models.ForeignKey(Articles, verbose_name="Новость", related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Пользователь", null=True, on_delete=models.SET_NULL)
    content = models.CharField("Содержание", max_length=512)
    date_create = models.DateTimeField("Дата создания", auto_now_add=True, blank=True)
