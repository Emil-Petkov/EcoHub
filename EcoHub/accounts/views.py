from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')