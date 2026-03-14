from django.shortcuts import render, redirect
from .models import Book

def book_page(request):
    books = Book.objects.all() 
    return render(request, 'book_list.html',)

def create_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")
        print(name)
        print(author)
        data = {"name":name, "author":author}
        Book.objects.create(name=name, author=author)
        return redirect('book_list')

    return render(request, 'create_book.html')

