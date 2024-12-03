from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Product
from .forms import ProductForm


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
    all_categories = ['bee honey', 'milk', 'fruits', 'vegetables', 'meat']
    categories_in_use = Product.objects.values_list('category', flat=True).distinct()
    return sorted(set(all_categories + [category.lower() for category in categories_in_use]))


class ProductListView(ListView):
    model = Product
    template_name = 'products/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        selected_category = self.request.GET.get('category', 'all').lower()
        min_price = float(self.request.GET.get('min_price', 0.01))
        max_price = float(self.request.GET.get('max_price', 999))

        queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        if selected_category != 'all':
            queryset = queryset.filter(category__iexact=selected_category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_categories()
        context['selected_category'] = self.request.GET.get('category', 'all').lower()
        context['min_price'] = self.request.GET.get('min_price', 0.01)
        context['max_price'] = self.request.GET.get('max_price', 999)
        context['empty_message'] = None
        if not context['products']:
            selected_category = context['selected_category']
            if selected_category != 'all':
                context['empty_message'] = f"The category '{selected_category}' is empty."
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/shop-detail.html'
    context_object_name = 'product'
