from django.db import models
from django.utils import timezone

# Create your models here.

#Definicmo la tabla de Categorias primero 

##### Tablas de Prueba #####
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria
    
class vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehiculo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
    
###### Tablas reales #######

# django_website/main/models.py
# django_website/main/models

class ArticleSeries(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default='', blank=True)
    slug = models.SlugField("Series slug", null=False, blank=False, unique=True)
    published = models.DateTimeField('Date published', default=timezone.now)

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, default="", blank=True)
    article_slug = models.SlugField("Article slug", null=False, blank=False, unique=True)
    content = models.TextField()
    published = models.DateTimeField("Date published", default=timezone.now)
    modified = models.DateTimeField("Date modified", default=timezone.now)
    series = models.ForeignKey(ArticleSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']

    