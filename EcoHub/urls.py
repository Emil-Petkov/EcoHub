from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('EcoHub.common.urls')),
    path('products/', include('EcoHub.products.urls')),
    path('orders/', include('EcoHub.orders.urls')),
    path('accounts/', include('EcoHub.accounts.urls')),
    path('reviews/', include('EcoHub.reviews.urls')),
]

handler404 = 'EcoHub.common.views.error_404'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)