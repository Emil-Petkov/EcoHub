from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView, LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, UpdateView, FormView

from .forms import UpdateProfilePictureForm, UpdateEmailForm, UpdatePhoneForm, UpdateAddressForm, UpdateAboutForm, \
    CustomUserCreationForm
from django.contrib import messages

from .utils import get_google_maps_url
from django.contrib.auth import get_user_model

from ..products.models import Product
import logging

User = get_user_model()


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
        context['products'] = Product.objects.filter(user=user)
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
        return ['accounts/update_profile.html']

    def get_form_class(self):
        form_mapping = {
            # 'profile_picture': UpdateProfilePictureForm,
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


@method_decorator(login_required, name='dispatch')
class MyProfileView(View):
    def get(self, request):
        form = UpdateProfileForm(instance=request.user)
        return render(request, 'accounts/my-profile.html', {'form': form})

    def post(self, request):
        form = UpdateProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
        else:
            messages.error(request, "Failed to update profile. Please check the errors.")
        return redirect('my_profile')


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


class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'accounts/password_reset.html')

    def post(self, request):
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            request.session['reset_user_id'] = user.id
            return redirect('password_reset_confirm')
        except User.DoesNotExist:
            messages.error(request, 'Username not found.')
            return redirect('password_reset')


class SetNewPasswordView(View):
    def get(self, request):
        if 'reset_user_id' not in request.session:
            return redirect('password_reset')
        return render(request, 'accounts/password_reset_confirm.html')

    def post(self, request):
        user_id = request.session.get('reset_user_id')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        from django.core.exceptions import ValidationError
        from django.contrib.auth.password_validation import validate_password

        try:
            validate_password(new_password)
        except ValidationError as e:
            messages.error(request, ' '.join(e.messages))
            return redirect('password_reset_confirm')

        if new_password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('password_reset_confirm')

        try:
            user = User.objects.get(id=user_id)
            user.password = make_password(new_password)
            user.save()
            del request.session['reset_user_id']
            messages.success(request, 'Password reset successfully. You can now log in.')
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'An error occurred.')
            return redirect('password_reset')


class DeleteProductView(View):
    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id, user=request.user)
            product.delete()
            messages.success(request, 'Product deleted successfully.')
        except Product.DoesNotExist:
            messages.error(request, 'Product not found or you do not have permission to delete this product.')
        return redirect('manage_products')


class MyProductsView(TemplateView):
    template_name = 'accounts/my-products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['MEDIA_URL'] = settings.MEDIA_URL
        context['products'] = Product.objects.filter(user=user)
        context['google_maps_url'] = get_google_maps_url(
            getattr(user, 'address', "Default Location")
        )
        return context


logger = logging.getLogger(__name__)

# @login_required
# def update_profile_picture(request):
#     if request.method == "POST":
#         user = request.user
#         if 'profile_picture' in request.FILES:
#             logger.info(f"Uploading new profile picture for user: {user.username}")
#             user.profile_picture = request.FILES['profile_picture']
#         else:
#             logger.warning(f"No file uploaded. Setting default profile picture for user: {user.username}")
#             user.profile_picture = 'users/profile_pictures/default-profile.jpg'
#         user.save()
#         logger.info(f"Profile picture updated successfully for user: {user.username}")
#         return redirect('profile')
