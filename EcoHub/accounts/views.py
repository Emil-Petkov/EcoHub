from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')  # Форма за вход (ако я имаш)

def register_view(request):
    return render(request, 'register.html')  # Форма за регистрация (ако я имаш)

def profile_view(request):
    return render(request, 'profile.html')  # Профил на потребителя (ако я имаш)
