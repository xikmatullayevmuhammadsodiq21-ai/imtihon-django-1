from django.shortcuts import render, redirect

def login_page(request):
    if request.method == "POST":
        return redirect('book_list')
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        return redirect('login')
    return render(request, 'register.html')