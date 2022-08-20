from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Avatar = models.ImageField('Пользовательское фото', null=True, blank=True, upload_to='media/img')
    Patronymic = models.CharField('Отчество', max_length=40, default='', null=True, blank=True)
    Date_of_birth = models.DateField('Дата рождения', null=True, blank=True)

    def __abs__(self):
        return self.user

    def get_absolute_url(self):
        return f'/{self.id}/edit'
    @property
    def photo_url(self):
        if self.Avatar and hasattr(self.Avatar, 'url'):
            return self.Avatar.url



    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователей'