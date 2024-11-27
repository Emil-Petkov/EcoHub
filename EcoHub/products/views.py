from django.shortcuts import render

def shop(request):
    return render(request, 'shop.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')
