# Generated by Django 4.0.5 on 2022-07-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='', max_length=255, verbose_name='Описание статьи'),
            preserve_default=False,
        ),
    ]