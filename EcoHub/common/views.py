from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def error_404(request, exception):
    return render(request, '404/404.html', status=404)