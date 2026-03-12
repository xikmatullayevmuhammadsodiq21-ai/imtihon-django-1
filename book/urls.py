from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.book_page, name='book_list'),
    path('create_book/', views.create_page, name='create_book'),
]
