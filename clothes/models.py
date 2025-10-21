from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Clothing(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название одежды')
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    image = models.URLField(verbose_name='Фото')
    categories = models.ManyToManyField(Category, related_name='clothes', verbose_name='Категория')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'одежду'
        verbose_name_plural = 'одежда'
