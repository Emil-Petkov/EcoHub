from django.shortcuts import render

def order_list(request):
    return render(request, 'cart.html')  # Количка за поръчки

def order_detail(request, pk):
    return render(request, 'checkout.html')  # Детайли за поръчка
