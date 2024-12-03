from django import forms
from .models import Product

CATEGORY_CHOICES = [
    ('bee honey', 'Bee Honey'),
    ('milk', 'Milk'),
    ('fruits', 'Fruits'),
    ('vegetables', 'Vegetables'),
    ('meat', 'Meat'),
]


class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Product
        fields = ['name', 'category', 'unit', 'description', 'price', 'image']
