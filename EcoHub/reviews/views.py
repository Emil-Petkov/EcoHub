from django.shortcuts import render

def review_list(request, product_id):
    return render(request, 'testimonial.html')  # Отзиви за продукт

def add_review(request, product_id):
    return render(request, 'add-review.html')  # Форма за добавяне на отзив (ако я имаш)
