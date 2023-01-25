# Generated by Django 3.2 on 2023-01-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_rename_recipe_favouriterecipe_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_en',
            field=models.TextField(null=True, verbose_name='Готовка'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cooking_ru',
            field=models.TextField(null=True, verbose_name='Готовка'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя рецепта'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Имя рецепта'),
        ),
    ]