from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace="home")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('products/', include('products.urls', namespace="products")),
    path('cart/', include('cart.urls', namespace="cart")),
    path('auth/', include('allauth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
