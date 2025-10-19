from django.db import models

class Films(models.Model):
    image = models.ImageField(upload_to='films/', verbose_name='загрузите картинку фильма')
    title = models.CharField(max_length=100,verbose_name='напишите название фильма')
    description = models.TextField(verbose_name='укажите описание к фильму')
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Фантастика','Фантастика'),
        ('Боевики','Боевики')
    )

    # default = аттрибут по умолчанию
    genre = models.CharField(max_length=100, choices=GENRE, default='Фантастика')
    #blank = True поле не обязательно для заполнения 
    director = models.CharField(max_length=100, blank=True, verbose_name='Укажите режиссера')
    quantity = models.PositiveBigIntegerField(default=1, verbose_name='Укажите количество серий')
    trailer = models.URLField(verbose_name='укажите ссылку с Youtube')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    # Посмотреть документацию django-models

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'фильмы'
        verbose_name_plural = 'фильмы'

