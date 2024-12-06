from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    payment_method = forms.ChoiceField(
        choices=[('cash', 'Cash on Delivery'), ('card', 'Credit/Debit Card')],
        widget=forms.RadioSelect
    )
    card_number = forms.CharField(required=False, max_length=16)
    card_expiry = forms.CharField(required=False, max_length=5)
    card_cvv = forms.CharField(required=False, max_length=3)

    class Meta:
        model = Order
        fields = ['full_name', 'address', 'phone', 'email', 'payment_method', 'card_number', 'card_expiry', 'card_cvv']

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('payment_method')
        if payment_method == 'card':
            if not cleaned_data.get('card_number'):
                self.add_error('card_number', 'Card number is required for card payment.')
            if not cleaned_data.get('card_expiry'):
                self.add_error('card_expiry', 'Card expiry date is required for card payment.')
            if not cleaned_data.get('card_cvv'):
                self.add_error('card_cvv', 'Card CVV is required for card payment.')
        return cleaned_data
