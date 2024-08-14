from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.book_form, name='book_form'),
    path('books/', views.book_list, name='book_list'),
]
