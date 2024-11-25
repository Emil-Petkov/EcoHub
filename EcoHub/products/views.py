from django.shortcuts import render

def product_list(request):
    return render(request, 'shop.html')  # Списък с продукти

def product_detail(request, pk):
    return render(request, 'shop-detail.html')  # Детайли за продукт

def add_product(request):
    return render(request, 'add-product.html')  # Форма за добавяне на продукт (ако я имаш)
