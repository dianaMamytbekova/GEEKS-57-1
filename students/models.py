from django.db import models

class Student(models.Model):
    SUBJECT = (
        ('Программирование','Программирование'),
        ('Математика','Математика'),
        ('Химия','Химия'),
        ('Биология','Биология')
    )
    name = models.CharField(max_length=100, verbose_name='Как тебя зовут:')
    date_of_birth = models.DateField(verbose_name='Укажи дату рождения:')
    application = models.CharField(verbose_name='На кого ты учишься:')
    instagram = models.URLField(verbose_name='Укажи ссылку на Инстаграм')
    subject = models.CharField(max_length=100, choices=SUBJECT,  verbose_name='Какой твой любимый предмет')
    photo = models.URLField(verbose_name='Укажите ссылку на фото')
    education = models.FileField(upload_to='students/', verbose_name='Загрузите ваш диплом', blank=True)

    
