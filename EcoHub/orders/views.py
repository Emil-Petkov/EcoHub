from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from EcoHub.products.models import Product
from .models import Cart
from django.http import HttpResponse
from .forms import CheckoutForm
import json




class CartView(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'order/my_bag.html'
    context_object_name = 'cart_items'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = sum(item.product.price * item.quantity for item in self.get_queryset())
        return context

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


@login_required(login_url='/accounts/login/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('my_bag')


@login_required(login_url='/accounts/login/')
def delete_cart_item(request, product_id):
    Cart.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('my_bag')


def update_cart(request, product_id):
    if request.method == 'POST':
        try:
            cart_item = Cart.objects.get(product_id=product_id, user=request.user)

            data = json.loads(request.body)
            action = data.get('action')

            if action == 'increase':
                cart_item.quantity += 1
            elif action == 'decrease' and cart_item.quantity > 1:
                cart_item.quantity -= 1

            cart_item.save()

            cart_items = Cart.objects.filter(user=request.user)
            subtotal = sum(item.product.price * item.quantity for item in cart_items)
            shipping = 0 if subtotal >= 30 else 5.00
            total = subtotal + shipping

            return JsonResponse({
                'quantity': cart_item.quantity,
                'total_price': cart_item.product.price * cart_item.quantity,
                'subtotal': subtotal,
                'shipping': "Free shipping" if subtotal >= 30 else shipping,
                'total': total,
            })
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Item not found in cart'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required(login_url='/accounts/login/')
def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            Cart.objects.filter(user=request.user).delete()
            return HttpResponse("Your order has been placed successfully!")
    else:
        form = CheckoutForm()

    return render(request, 'order/checkout.html', {'form': form, 'cart_items': Cart.objects.filter(user=request.user)})
