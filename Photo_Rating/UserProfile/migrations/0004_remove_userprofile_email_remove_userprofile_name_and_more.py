# Generated by Django 4.0.2 on 2022-03-30 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0003_alter_userprofile_options_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='New_password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Repeat_the_password',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Surname',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='UserName',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Пользовательское фото'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Patronymic',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Отчество'),
        ),
    ]