from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UpdateProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email

class UpdateEmailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']

class UpdatePhoneForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone']

class UpdateAddressForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['address']

class UpdateAboutForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['about']
