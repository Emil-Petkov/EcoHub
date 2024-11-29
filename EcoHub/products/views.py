from django.shortcuts import render

def shop(request):
    return render(request, 'shop.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def add_product(request):
    return  render(request, 'products/add-product.html')