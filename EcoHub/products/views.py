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

class ProductListView(ListView):
    model = Product
    template_name = 'products/shop.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/shop-detail.html'
    context_object_name = 'product'
