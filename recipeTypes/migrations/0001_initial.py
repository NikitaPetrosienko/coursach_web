# Generated by Django 4.0.5 on 2022-06-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeType', models.CharField(max_length=255, verbose_name='Тип рецепта')),
            ],
            options={
                'verbose_name': 'Тип рецепта',
                'verbose_name_plural': 'Типы рецепта',
            },
        ),
    ]
