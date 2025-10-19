from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

#ListView
def film_list_view(request):
    if request.method == 'GET':
        films = models.Films.objects.all()
        context = {
            'films': films,
        }
        return render(request, template_name='films/films_list.html', context=context)
    
#DetailView
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Films, id=id)
        context = {
           'film_id': film_id,
        }
        return render(request, template_name='films/film_detail.html',context=context)
    



def first_message_view(request):
    if request.method == 'GET':
        return HttpResponse('Привет Geeks!')
    

    
def second_message_view(request):
    if request.method == 'GET':
        return HttpResponse('Второй текст')    
