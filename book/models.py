from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    image = models.ImageField(upload_to='book/', verbose_name='загрузите обложку книги')
    title = models.CharField(max_length=100, verbose_name='напишите название книги')
    description = models.TextField(verbose_name='укажите описание к книге')
    quantity_page = models.PositiveBigIntegerField(verbose_name='количество страниц')
    author = models.CharField(max_length=100, verbose_name='автор')
    book_audio = models.URLField(verbose_name='ссылка на аудиокнигу', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'


class Reviews(models.Model):
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name='reviews' )
    mark = models.PositiveIntegerField(verbose_name='Поставьте оценку от 1 до 5', 
                                       validators=[MaxValueValidator(5),MinValueValidator(1)])
    review_text = models.TextField(default='Хорошая книга')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_book} - {self.mark}'
    
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'


class Person(models.Model):
    name = models.CharField(max_length=100, default='Антон')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Tour(models.Model):
    tourist = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='tour')
    title = models.CharField(max_length=100, verbose_name='название тура')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tourist.name} - {self.title}'

    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'        