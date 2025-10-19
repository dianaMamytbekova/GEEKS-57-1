from django.db import models


class Book(models.Model):
    image = models.ImageField(upload_to='book/', verbose_name='загрузите обложку книги')
    title = models.CharField(max_length=100, verbose_name='напишите название фильма')
    description = models.TextField(verbose_name='укажите описание к фильму')
    quantity_page = models.PositiveBigIntegerField(verbose_name='количество страниц')
    author = models.CharField(max_length=100, verbose_name='автор')
    book_audio = models.URLField(verbose_name='ссылка на аудиокнигу', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'