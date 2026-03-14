from django.shortcuts import render, redirect

books = []

def book_page(request):
    return render(request, 'book_list.html', {"books": books})

def create_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        author = request.POST.get("author")

        books.append({
            "name": name,
            "author": author
        })

        return redirect('book_list')

    return render(request, 'create_book.html')


def delete_book(request, index):
    books.pop(index)
    return redirect('book_list')