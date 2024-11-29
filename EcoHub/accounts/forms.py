from django import forms
from .models import CustomUser

class UpdateProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']

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
