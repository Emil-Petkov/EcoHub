from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import (
    UpdateProfilePictureForm, UpdateEmailForm,
    UpdatePhoneForm, UpdateAddressForm, UpdateAboutForm
)
from .utils import get_google_maps_url


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CustomLoginView(LoginView):
    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me', False)
        if remember_me:
            self.request.session.set_expiry(1209600)
        else:
            self.request.session.set_expiry(0)
        return super().form_valid(form)


@login_required
def manage_products(request):
    user = request.user
    google_maps_url = get_google_maps_url(user.address if user.address else "Default Location")
    return render(request, 'accounts/manage-products.html', {
        'user': user,
        'google_maps_url': google_maps_url,
    })


@login_required
def update_profile_picture(request):
    if request.method == 'POST':
        form = UpdateProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture updated successfully!')
            return redirect('manage_products')
    else:
        form = UpdateProfilePictureForm(instance=request.user)
    return render(request, 'accounts/update_profile_picture.html', {'form': form})


@login_required
def update_email(request):
    if request.method == 'POST':
        form = UpdateEmailForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Email updated successfully!')
            return redirect('manage_products')
    else:
        form = UpdateEmailForm(instance=request.user)
    return render(request, 'accounts/update_email.html', {'form': form})


@login_required
def update_phone(request):
    if request.method == 'POST':
        form = UpdatePhoneForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Phone number updated successfully!')
            return redirect('manage_products')
    else:
        form = UpdatePhoneForm(instance=request.user)
    return render(request, 'accounts/update_phone.html', {'form': form})


@login_required
def update_address(request):
    if request.method == 'POST':
        form = UpdateAddressForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully!')
            return redirect('manage_products')
    else:
        form = UpdateAddressForm(instance=request.user)
    return render(request, 'accounts/update_address.html', {'form': form})


@login_required
def update_about(request):
    if request.method == 'POST':
        form = UpdateAboutForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'About section updated successfully!')
            return redirect('manage_products')
    else:
        form = UpdateAboutForm(instance=request.user)
    return render(request, 'accounts/update_about.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')


def login_view(request):
    return render(request, 'accounts/login.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def my_products(request):
    return render(request, 'accounts/my-products.html')


@login_required
def my_profile(request):
    return render(request, 'accounts/my-profile.html')


