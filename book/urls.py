from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.book_page, name='book_list'),
    path('create_book/', views.create_page, name='create_book'),
]