from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EcoHub.common.urls')),
    path('products/', include('EcoHub.products.urls')),
    path('accounts/', include('EcoHub.accounts.urls')),
    path('orders/', include('EcoHub.orders.urls')),
    path('reviews/', include('EcoHub.reviews.urls')),
]
