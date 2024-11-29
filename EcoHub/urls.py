from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EcoHub.common.urls')),
    path('products/', include('EcoHub.products.urls')),
    path('orders/', include('EcoHub.orders.urls')),
    path('accounts/', include('EcoHub.accounts.urls')),
    path('reviews/', include('EcoHub.reviews.urls')),

    path('accounts/', include('EcoHub.accounts.urls')),
]

handler404 = 'EcoHub.common.views.error_404'

