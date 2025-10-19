from django.shortcuts import render, get_object_or_404
from . import models

def book_list_view(request):
    if request.method == 'GET':  
        books = models.Book.objects.all()  
        context = {
            'books': books  
        }
        return render(request, 'book/book_list.html', context)


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)  
        context = {
            'book_id': book_id
        }
        return render(request, 'book/book_detail.html', context)


