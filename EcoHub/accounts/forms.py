from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()



class UpdateEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Enter a valid email address.',
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email address is already in use.")
        return email


class UpdatePhoneForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone']

    phone = forms.CharField(
        max_length=15,
        required=False,
        help_text='Enter a valid phone number.',
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone and not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")
        return phone


class UpdateAddressForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['address']

    address = forms.CharField(
        max_length=255,
        required=False,
        help_text='Enter your address.',
    )


class UpdateAboutForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['about']

    about = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text='Write something about yourself.',
    )


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
