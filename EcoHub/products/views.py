from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import ProductForm


from django.shortcuts import render
from .models import Product

def shop_view(request):
    sort_by = request.GET.get('sort', 'default')
    products = Product.objects.all()

    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')

    return render(request, 'products/shop.html', {
        'products': products,
        'sort_by': sort_by,
    })



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'accounts/add_product.html'
    success_url = reverse_lazy('shop')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error adding product. Please try again.")
        return super().form_invalid(form)



def get_categories():
    all_categories = {'bee honey', 'milk', 'fruits', 'vegetables', 'meat'}
    categories_in_use = Product.objects.values_list('category', flat=True).distinct()
    return sorted(all_categories.union(set(category.lower() for category in categories_in_use)))


class ProductListView(ListView):
    model = Product
    template_name = 'products/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_categories = self.request.GET.getlist('categories')
        min_price = float(self.request.GET.get('min_price', 0.01))
        max_price = float(self.request.GET.get('max_price', 999))

        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        if selected_categories:
            queryset = queryset.filter(category__in=selected_categories)
        return queryset



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_categories()
        context['selected_categories'] = self.request.GET.getlist('categories')
        context['min_price'] = self.request.GET.get('min_price', 0.01)
        context['max_price'] = self.request.GET.get('max_price', 999)
        context['sort_by'] = self.request.GET.get('sort', 'default')
        context['empty_message'] = None
        if not context['products']:
            context['empty_message'] = "No products match your filters."
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/shop-detail.html'
    context_object_name = 'product'
