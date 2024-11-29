from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'accounts/login.html')

def register_view(request):
    return render(request, 'accounts/register.html')

def my_products(request):
    return render(request, 'accounts/my-products.html')

def my_profile(request):
    return render(request, 'accounts/my-profile.html')

@login_required
def manage_products(request):
    user = request.user
    return render(request, 'accounts/manage-products.html', {
        'user': user,
    })
