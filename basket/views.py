from django.shortcuts import render, redirect, get_object_or_404
from .models import Basket
from .forms import BasketForm


def create_order(request):
    if request.method == 'POST':
        form = BasketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = BasketForm()
    return render(request, 'basket/create_order.html', {'form': form})


def order_list(request):
    orders = Basket.objects.all()
    return render(request, 'basket/order_list.html', {'orders': orders})


def update_order(request, id):
    order = get_object_or_404(Basket, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = BasketForm(instance=order)
    return render(request, 'basket/update_order.html', {'form': form})


def delete_order(request, id):
    order = get_object_or_404(Basket, id=id)
    order.delete()
    return redirect('order_list')
