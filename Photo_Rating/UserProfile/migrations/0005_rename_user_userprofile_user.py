# Generated by Django 4.0.2 on 2022-03-30 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0004_remove_userprofile_email_remove_userprofile_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='User',
            new_name='user',
        ),
    ]
