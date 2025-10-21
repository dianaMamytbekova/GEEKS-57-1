from django.db import models
from book.models import Book 


class Basket(models.Model):
    buyer_name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    buyer_email = models.EmailField(verbose_name='Email покупателя')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Выберите книгу')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer_name} — {self.book.title}"

