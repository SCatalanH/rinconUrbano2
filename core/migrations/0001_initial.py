# Generated by Django 4.2 on 2023-04-19 03:24

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('article_slug', models.SlugField(unique=True, verbose_name='Article slug')),
                ('content', tinymce.models.HTMLField(blank=True, default='')),
                ('notes', tinymce.models.HTMLField(blank=True, default='')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date modified')),
            ],
            options={
                'verbose_name_plural': 'Article',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('slug', models.SlugField(unique=True, verbose_name='Series slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
            ],
            options={
                'verbose_name_plural': 'Series',
                'ordering': ['-published'],
            },
        ),
    ]
