from django.shortcuts import render
from .models import Clothing, Category

def all_clothes(request):
    search_query = request.GET.get('q', '')
    if search_query:
        clothes = Clothing.objects.filter(title__icontains=search_query)
    else:
        clothes = Clothing.objects.all()
    return render(request, 'clothes/all_clothes.html', {'clothes': clothes})


def men_clothes(request):
    category = Category.objects.get(name='одежда мужская')
    clothes = Clothing.objects.filter(categories=category)
    return render(request, 'clothes/men_clothes.html', {'clothes': clothes})

def women_clothes(request):
    category = Category.objects.get(name='одежда женская')
    clothes = Clothing.objects.filter(categories=category)
    return render(request, 'clothes/women_clothes.html', {'clothes': clothes})

def kids_clothes(request):
    category = Category.objects.get(name='детская одежда')
    clothes = Clothing.objects.filter(categories=category)
    return render(request, 'clothes/kids_clothes.html', {'clothes': clothes})
