# Generated by Django 4.0.5 on 2022-06-21 14:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles_comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecomment',
            name='author_id',
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]