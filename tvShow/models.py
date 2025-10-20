from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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



class Reviews(models.Model):
    choice_film = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='reviews')
    mark = models.PositiveBigIntegerField(verbose_name='поставьте оценку от 1 до 5',
                                           validators=[MaxValueValidator(5),MinValueValidator(1)])
    review_text = models.TextField(default='Прикольный фильм')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_film} - {self.mark}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'



class Person(models.Model):
    name = models.CharField(max_length=100, default='Антон')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автовладелец'    
        verbose_name_plural = 'Автовладельцы'



class Car(models.Model):
    passport = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='driver')    
    brand_car = models.CharField(max_length=100, default='bmw m3 g30')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.brand_car} - {self.passport.name}'
    
    class Meta:
        verbose_name = 'машину'
        verbose_name_plural = 'машины'



