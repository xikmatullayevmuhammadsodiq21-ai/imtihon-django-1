from django.shortcuts import render

# Create your views here.
def book_page(request):
    return render(request, 'book_list.html')

def create_page(request):
    return render(request, 'create_book.html')