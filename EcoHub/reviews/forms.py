from EcoHub.reviews.models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'comment', 'satisfaction']
