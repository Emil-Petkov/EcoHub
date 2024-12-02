from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, FormView
from .forms import (
    UpdateProfilePictureForm, UpdateEmailForm,
    UpdatePhoneForm, UpdateAddressForm, UpdateAboutForm, CustomUserCreationForm
)
from .utils import get_google_maps_url
from django.contrib.auth.models import User


class ManageProductsView(TemplateView):
    template_name = 'accounts/manage-products.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['google_maps_url'] = get_google_maps_url(
            getattr(user, 'address', "Default Location")
        )
        return context


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CustomLoginView(LoginView):
    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me', False)
        self.request.session.set_expiry(1209600 if remember_me else 0)
        return super().form_valid(form)


class ProfileUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('manage_products')

    def get_object(self, queryset=None):
        return self.request.user

    def get_template_names(self):
        field_template_mapping = {
            'profile_picture': 'accounts/update_profile_picture.html',
            'email': 'accounts/update_email.html',
            'phone': 'accounts/update_phone.html',
            'address': 'accounts/update_address.html',
            'about': 'accounts/update_about.html',
        }
        return [field_template_mapping.get(self.kwargs['field'])]

    def get_form_class(self):
        form_mapping = {
            'profile_picture': UpdateProfilePictureForm,
            'email': UpdateEmailForm,
            'phone': UpdatePhoneForm,
            'address': UpdateAddressForm,
            'about': UpdateAboutForm,
        }
        return form_mapping.get(self.kwargs['field'])

    def form_valid(self, form):
        messages.success(self.request, f"{self.kwargs['field'].capitalize()} updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"Failed to update {self.kwargs['field']}. Please try again.")
        return super().form_invalid(form)


class MyProductsView(TemplateView):
    template_name = 'accounts/my-products.html'


class MyProfileView(TemplateView):
    template_name = 'accounts/my-profile.html'


class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registration successful. You can now log in.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))