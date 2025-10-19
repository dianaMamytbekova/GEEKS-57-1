from django.urls import path
from . import views

urlpatterns = [
    path('',views.film_list_view, name='films_list'),
    path('film_detail/<int:id>/',views.film_detail_view, name='films_detail'),
    path('first_message/', views.first_message_view, name='first_message'),
    path('second_message/', views.second_message_view, name='second_message'),
]


